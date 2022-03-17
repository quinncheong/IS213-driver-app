from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', api_version=(0,1,0))
for message in consumer:
    print (message)