#!/usr/bin/python

import pika

credentials = pika.credentials.PlainCredentials('admin','admin')

parameters = pika.ConnectionParameters(host='192.168.32.131',credentials=credentials)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.queue_declare(queue='hzw-hello')


while true:
    msbody = input("msg:")
    channel.basic_publish(exchange='', routing_key='hzwhelloqueue', body=msbody)
    print(" [x] Sent '%s'" % (msbody))
connection.close()

#
# if __name__ == '__main__':
#     print(123)
