#!/usr/bin/python
# coding=utf-8

import pika
import time


queue_name='hzw_queue'

credentials = pika.credentials.PlainCredentials('admin','admin')

parameters = pika.ConnectionParameters(host='192.168.32.131',credentials=credentials)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

def dowork(message):
    message=str(message)

    if 'exception' in message:
        1 / 0

    for itemChar in message:
        if itemChar == '.':
            time.sleep(1)

    print(str(bytes(message, 'GBK'  ), 'GBK'  ))
    print(str(bytes(message, 'UTF-8'), 'UTF-8'))






def callback(channel, method, properties, body):
    message = str(body, "UTF-8")
    print("[x] Received %r %r" % (message,time.time()))
    try:
        dowork(message)
        print("[x] Done %r %r" % (message, time.time()))
    except:
        print("[x] Done_except %r %r" % (message, time.time()))
    finally:
        channel.basic_ack(method.delivery_tag)      # 自定义响应


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,on_message_callback=callback)
channel.start_consuming()


