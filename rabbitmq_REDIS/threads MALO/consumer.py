import pika
import redis
import csv

# Conexión con REDIS
redis_client = redis.Redis(host='localhost', port=6379)

def on_message_received(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f"Received new message: {message}")

    # Guardado en REDIS
    redis_client.rpush('messages', message)

    # Exportar CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message])

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
