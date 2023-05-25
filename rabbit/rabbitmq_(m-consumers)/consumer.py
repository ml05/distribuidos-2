import pika, sys, os

def callback(ch, method, properties, body):
    sender = properties.headers.get('sender')
    print("Device", sender, "sending:", body.decode('utf-8'))

def receive_message(consumer_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(f'Consumer {consumer_id} is waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        consumer_id = sys.argv[1]  # Obtener el ID del consumidor desde los argumentos de línea de comandos
        receive_message(consumer_id)
    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
