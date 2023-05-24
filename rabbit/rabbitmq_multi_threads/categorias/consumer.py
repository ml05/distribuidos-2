import pika
import sys
import os

def callback(ch, method, properties, body):
    categoria = method.routing_key
    print("Device", categoria, "sending:", body.decode('utf-8'))

def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    categorias = ['temperatura', 'humedad', 'pH', 'luminosidad', 'CO2']

    for categoria in categorias:
        channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=categoria)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print('Consumer is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        receive_message()
    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
