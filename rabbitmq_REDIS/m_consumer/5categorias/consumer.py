import pika
import sys
import os
import redis
import time
import csv

# Configuración de Redis
redis_host = 'localhost'
redis_port = 6379
redis_db = 0

# Configuración del archivo CSV
csv_filename = 'data.csv'

# Conexión a Redis
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

def callback(ch, method, properties, body):
    categoria = method.routing_key
    message = body.decode('utf-8')
    print(f"Device {categoria} sending: {message}")

    # Guardar en Redis y medir el tiempo de guarda
    start_time = time.time()
    result = redis_client.set(categoria, message)
    end_time = time.time()
    execution_time = end_time - start_time

    # Verificar si se guardó correctamente en Redis
    if result>0:
        print("Saved to Redis successfully.")
    else:
        print("Failed to save to Redis.")

    # Exportar a CSV
    export_to_csv(categoria, message, execution_time)

def export_to_csv(categoria, message, execution_time):
    with open(csv_filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([categoria, message, execution_time])

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
