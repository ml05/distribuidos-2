import pika

def on_message_received(ch, method, properties, body):
    print(f"Received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

try:
    channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

    print("Starting Consuming")

    channel.start_consuming()
except KeyboardInterrupt:
    # Capturar la excepción "KeyboardInterrupt" y detener la consumición de mensajes
    channel.stop_consuming()

connection.close()

