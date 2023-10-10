from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(bootstrap_servers='kafka-broker-headless:9092')
producer.send('me', b'some_message_bytes')