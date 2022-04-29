from time import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

# Hardcoded for now but must change
bootstrap_server = 'kafka:9093' 
kafka_topic = 'twilio-msg'

# This file serves as the outline for the Kafka Producer.
# We are using a kafka-python wrapper on top of the native kafka built by apache
# To understand the functions, read BOTH the kafka-python docs and the apache kafka docs

# Message should be in a json format
def send_message(message):
    print('initialised producer')
    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_server], 
        value_serializer=lambda m: json.dumps(m).encode('ascii'), 
        retries=2   
    )
    # Async by default, but we must call .get on the future to ensure 'thread-level' blocking
    future = producer.send(kafka_topic, message)

    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        print('Producer Request has failed')
        return False
        pass

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

    print('end')

    return True

# # Asynchronous by default
# future = producer.send('test-topic-2', b'{"hello": "world"}')


# # produce keyed messages to enable hashed partitioning
# producer.send('my-topic', key=b'foo', value=b'bar')

# # encode objects via msgpack
# producer = KafkaProducer(value_serializer=msgpack.dumps)
# producer.send('msgpack-topic', {'key': 'value'})



# # produce asynchronously
# for _ in range(100):
#     producer.send('my-topic', b'msg')

# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)

# def on_send_error(excp):
#     log.error('I am an errback', exc_info=excp)
#     # handle exception

# # produce asynchronously with callbacks
# producer.send('my-topic', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# # block until all async messages are sent
# producer.flush()

# # configure multiple retries
# producer = KafkaProducer(retries=5)