#!/usr/bin/env python
import pika
import redis
import time
import csv

# Conexión a Redis
redis_client = redis.Redis(host='localhost', port=6379)

def callback(ch, method, properties, body):
    sender = properties.headers.get('sender')
    message = body.decode('utf-8')
    print("Device", sender, "sending:", message)

    # Guardar el mensaje en Redis
    start_time = time.time()
    result = redis_client.set(sender, message)
    end_time = time.time()
    Tredis = end_time - start_time

    # Verificar si el mensaje se guardó 
    if result>0:
        print("El mensaje se ha guardado correctamente en Redis")
    else:
        print("Error al guardar el mensaje en Redis")

    print("Tiempo de ejecución:", Tredis)

    # Exporta los datos a un archivo CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message, Tredis])

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', 
                          on_message_callback=callback, 
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' Interrupted')
