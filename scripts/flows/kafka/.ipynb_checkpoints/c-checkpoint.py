from client import KafkaObject
obj = KafkaObject(bootstrap_servers="broker:29092")
obj.consumer(["panos"], "aces-mini")