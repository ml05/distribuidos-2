import pika
import sys
import os
import csv

def guardar_en_csv(categoria, message):
    filename = f"{categoria}.csv"
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([message])

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='sensor_data', exchange_type='topic')

    # Declara una cola temporal y exclusiva para este receptor
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Enlaza la cola a la clave de enrutamiento "temperatura"
    channel.queue_bind(exchange='sensor_data', queue=queue_name, routing_key='temperatura')

    def callback(ch, method, properties, body):
        sender = properties.headers.get('sender')
        message = body.decode('utf-8')
        print("Device", sender, "sending:", message)
        guardar_en_csv('temperatura', message)

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
