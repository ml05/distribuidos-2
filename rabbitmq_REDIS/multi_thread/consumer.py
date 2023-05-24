import pika
import sys
import os
import redis
import csv
import time

# Conexión a REDIS
redis_client = redis.Redis(host='localhost', port=6379)

def callback(ch, method, properties, body):
    sender = properties.headers.get('sender')
    message = body.decode('utf-8')
    print("Device", sender, "sending:", message)

    # Guardar en rEDIS
    start_time = time.time()
    result = redis_client.rpush('messages', message)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tiempo de guardado en Redis:", execution_time, "segundos")

    # Verificacion de guardado
    if result > 0: # sesupone que si se guarda correctamente result tiene que ser > 0
        print("El mensaje se ha guardado correctamente en Redis")
    else:
        print("Error al guardar el mensaje en Redis")

    # Exporta a CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([sender, message, execution_time])

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
        # Reemplazar CSV existente si lo hay
        if os.path.exists('data.csv'):
            os.remove('data.csv')
        receive_message(consumer_id)
    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
