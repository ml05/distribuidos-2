import pika
import csv
import sys
import os
import redis
import time

def guardar_en_csv(message, tiempo_guardado):
    filename = "data_humedad.csv"
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([message, tiempo_guardado])

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='sensor_data', exchange_type='topic')

    # Declara una cola temporal y exclusiva para este receptor
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Enlaza la cola a la clave de enrutamiento "humedad"
    channel.queue_bind(exchange='sensor_data', queue=queue_name, routing_key='humedad')

    # Conecta a Redis
    redis_client = redis.Redis(host='localhost', port=6379)

    def callback(ch, method, properties, body):
        sender = properties.headers.get('sender')
        message = body.decode('utf-8')
        print("Device", sender, "sending:", message)

        start_time = time.time()  # Tiempo inicial

        # Guarda en Redis
        redis_key = f"{sender}:message"
        redis_client.set(redis_key, message)

        elapsed_time = time.time() - start_time  # Tiempo transcurrido
        print("Tiempo de guardado en Redis:", elapsed_time, "segundos")

        # Verifica si se guardó correctamente
        if redis_client.get(redis_key).decode('utf-8') == message:
            print("Guardado en Redis: Correcto")
        else:
            print("Guardado en Redis: Error")

        guardar_en_csv(message, elapsed_time)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit, press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(' Interrupted')
        channel.stop_consuming()
        connection.close()
        sys.exit(0)

if __name__ == '__main__':
    main()
