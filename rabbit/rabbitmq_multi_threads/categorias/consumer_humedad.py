import pika
import json

def callback(ch, method, properties, body):
    sender = properties.headers.get('sender')
    print(f"Device {sender} sending: {body.decode('utf-8')}")

def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='humedad.*')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        receive_messages()
    except KeyboardInterrupt:
        print(' Interrupted')
