#!/usr/bin/python
# coding=utf-8

import pika

def send():

    credentials = pika.credentials.PlainCredentials('admin', 'admin')

    parameters = pika.ConnectionParameters(host='192.168.32.131', credentials=credentials)

    connection = pika.BlockingConnection(parameters=parameters)

    channel = connection.channel()

    channel.queue_declare(queue='hzw-hello')


    while True:
        msbody = input("msg:")

        if len(msbody)==0:
            msbody = "default message!!!"

        channel.basic_publish(exchange='', routing_key='hzw-hello', body=msbody)
        print(" [x] Sent '%s'" % (msbody))

    connection.close()


if __name__ == '__main__':
    send()

