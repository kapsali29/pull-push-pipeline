from kafka.client import KafkaObject

k = KafkaObject("broker:29092")
k.consumer(['tiny-example'], "tiny-sim")