import sys
import json
import logging
import confluent_kafka
from confluent_kafka import KafkaError, KafkaException


class KafkaObject(object):
    def __init__(
            self,
            bootstrap_servers,
            buffering_max_messages=2000000,
            session_timeout=1740000,
            max_pol_interval_ms=1750000,
            heartbeat_interval_ms=30000,
            connections_max_handle_ms=54000000,
            off_set_reset='earliest'
    ):
        self.bootstrap_servers = bootstrap_servers
        self.producer_conf = {
            'bootstrap.servers': self.bootstrap_servers,
            'queue.buffering.max.messages': buffering_max_messages
        }
        self.consumer_conf = {
            'bootstrap.servers': self.bootstrap_servers,
            'session.timeout.ms': session_timeout,
            'heartbeat.interval.ms': heartbeat_interval_ms,
            'connections.max.idle.ms': connections_max_handle_ms,
            'max.poll.interval.ms': max_pol_interval_ms,
            'fetch.wait.max.ms': 1000,
            'socket.keepalive.enable': 'true',
            'default.topic.config': {
                'auto.offset.reset': off_set_reset
            }
        }
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('kafka-object')

    def producer(
            self,
            msg,
            topic
    ):
        messages_overflow = 0
        producer = confluent_kafka.Producer(**self.producer_conf)
        try:
            producer.produce(topic, value=json.dumps(msg))
        except BufferError as e:
            messages_overflow += 1

        # checking for overflow
        self.logger.error(f'BufferErrors: {messages_overflow}')
        producer.flush()

    def consumer(
            self,
            list_of_topics,
            group_id
    ):
        consumer_config = self.consumer_conf
        consumer_config['group.id'] = group_id
        consumer = confluent_kafka.Consumer(**consumer_config)
        consumer.subscribe(list_of_topics)
        
        while True:
            self.logger.info("Waiting for incoming data...")
            msg = consumer.poll()
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        '%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    # Error
                    raise KafkaException(msg.error())
            else:
                self.logger.info(msg.value())


