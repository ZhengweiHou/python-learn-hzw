#!/usr/bin/python
# coding=utf-8

import pika
from pika import spec

import time

credentials = pika.PlainCredentials('admin','admin')

parameters = pika.ConnectionParameters(host='192.168.32.131',credentials=credentials)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.basic_qos(prefetch_count=1)


def callback(channel, method, properties, body):
    # 处理函数的参数类型如下
    # channel = pika.spec.Channel(channel)
    # deliver = pika.spec.Basic.Deliver(method)
    # pika.spec.Channel(channel)
    pika.spec.Basic.Deliver(method)
    pika.spec.Basic.Deliver(method)
    properties = pika.spec.BasicProperties(properties)
    print(properties)
    body = str(body,"UTF-8")
    time.sleep(3)
    print("[x] Received %r" % body)


channel.basic_consume(
    queue='hzw-hello',
    on_message_callback=callback,
    auto_ack=True                   # 自动确认，若不确认，消息被获取后会处于未确认状态，不会被队列丢弃
                      )

print(" [x] Awaiting requests")
channel.start_consuming()

# channel.queue_bind(queue='hzw-hello')



