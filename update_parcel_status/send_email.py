#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import json
import os

import amqp_setup
import pika
import json

def send_email(message):
    """ 
    message will be in the following form 
    {
        subject: "", // Plain Text
        body: "", // HTML String ok
        emails: [],
    }
    """
    amqp_setup.check_setup()
    email_message = json.dumps(message)

    print(email_message)

    amqp_setup.channel.basic_publish(
        exchange=amqp_setup.exchangename, 
        routing_key="parcelFail.email", 
        body=email_message, 
        properties=pika.BasicProperties(delivery_mode = 2)
    ) 

    return


