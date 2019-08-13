#!/usr/bin/python
# coding=utf-8

import pika
from pika import spec

""" Content-type "text/plain", deliveryMode 2 (persistent), priority zero """
PERSISTENT_TEXT_PLAIN = spec.BasicProperties(content_type='text/plain', delivery_mode=2, priority=0)

def send():

    queue_name='hzw_queue'

    credentials = pika.credentials.PlainCredentials('admin','admin')

    parameters = pika.ConnectionParameters(host='192.168.32.131',credentials=credentials)

    connection = pika.BlockingConnection(parameters=parameters)

    channel = connection.channel()

    # channel.exchange_declare(exchange="hzw-exchange",exchange_type="fanout") # exchange_type: direct, fanout, topic, headers

    channel.queue_declare(queue=queue_name)


    while True:
        msbody = input("msg:")

        if len(msbody)==0:
            msbody = "default message!!!"

        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=msbody,
            properties=PERSISTENT_TEXT_PLAIN
        )

        print(" [x] Sent '%r'" % (msbody))

    connection.close()


if __name__ == '__main__':
    send()

