import pika
import redis
import csv
import time

# Conexion a REDIS
redis_client = redis.Redis(host='localhost', port=6379)

def on_message_received(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f"Received new message: {message}")

    # Guardar en REDIS
    start_time = time.time()
    result = redis_client.rpush('messages', message)
    end_time = time.time()
    Tredis = end_time - start_time

    # Verificar si el mensaje se guardó correctamente en Redis
    if result > 0: # se supone que si se recibe se tiene un valor diferente a 0
        print("El mensaje se ha guardado correctamente en Redis")
    else:
        print("Error al guardar el mensaje en Redis")

    # Exporta a CSV
    timestamp = time.time()  # Obtener el timestamp actual
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message, Tredis, timestamp])

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
