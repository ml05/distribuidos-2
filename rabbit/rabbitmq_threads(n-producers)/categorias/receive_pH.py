import pika
import signal
import sys

def callback(ch, method, properties, body):
    categoria = method.routing_key
    print(f"[pH] Received message: {body}")

def signal_handler(sig, frame):
    print('Deteniendo la ejecución...')
    connection.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='pH')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Starting Consuming [pH]")

channel.start_consuming()
