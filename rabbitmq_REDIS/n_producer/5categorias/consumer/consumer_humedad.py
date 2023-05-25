import pika
import signal
import sys
import redis
import csv
import time, os

# Crea una conexión a Redis
redis_client = redis.Redis(host='localhost', port=6379)

def callback(ch, method, properties, body):
    categoria = method.routing_key
    message = body.decode('utf-8')
    print(f"[Humedad] Received message: {message}")

    # Guarda el mensaje en Redis y mide el tiempo de ejecución
    start_time = time.time()
    result = redis_client.rpush('data_humedad', message)
    end_time = time.time()
    execution_time = end_time - start_time

    # Verifica si el mensaje se guardó correctamente en Redis
    if result > 0:
        print("El mensaje se ha guardado correctamente en Redis")
    else:
        print("Error al guardar el mensaje en Redis")

    print("Tiempo de ejecución:", execution_time)

    # Exporta los datos a un archivo CSV
    timestamp = time.time()
    with open('data_humedad.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message, execution_time, timestamp])

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

channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='humedad')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Starting Consuming [HUMEDAD]")

# Borra el archivo CSV existente antes de comenzar
if os.path.exists('data_humedad.csv'):
    os.remove('data_humedad.csv')

channel.start_consuming()
