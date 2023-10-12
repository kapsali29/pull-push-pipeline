import confluent_kafka
import json
# Kafka Settings
BATCH_SIZE = 1000
BOOTSTRAP_SERVERS = 'broker:29092'
BUFFERING_MAX_MESSAGES = 2000000
def confluent_kafka_producer_performance():
    # Note that you need to set producer buffer to at least as large as number of messages
    # otherwise you'll get a buffer overflow and the sequential messages will be corrupted
    messages_overflow = 0
    conf = {'bootstrap.servers': BOOTSTRAP_SERVERS,
            'queue.buffering.max.messages': BUFFERING_MAX_MESSAGES
            }

    producer = confluent_kafka.Producer(**conf)
    try:
        producer.produce("sample", value=json.dumps({"msg":"hello"}))
    except BufferError as e:
        messages_overflow += 1

    # checking for overflow
    print('BufferErrors: ' + str(messages_overflow))

    producer.flush()

confluent_kafka_producer_performance()