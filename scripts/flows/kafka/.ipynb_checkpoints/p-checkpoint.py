from client import KafkaObject
obj = KafkaObject(bootstrap_servers="broker:29092")
obj.producer(msg={"msg": "martel"}, topic="panos")