import socket
import pika
import time
hostname = socket.gethostname()
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='nodes')


def callback(channel, method, properties, body):
    print "Recieved: {}".format(body)


channel.basic_consume(callback, queue='nodes', no_ack=True)
try:
    print "Starting to consume:"
    channel.start_consuming()
except Exception as e:
    print e
finally:
    channel.close()

