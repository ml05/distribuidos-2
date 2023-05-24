
import pika
import json
import time
import string
import random

def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def enviar_mensaje():
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='letterbox')

    # Crear el mensaje en el formato adecuado
    data = {
        "timestamp": time.time(),
        "value": {
            "data": generar_cadena_aleatoria(4)  # Generar una cadena aleatoria de longitud 4
        }
    }

    # Convertir el mensaje a formato JSON
    json_message = json.dumps(data)

    channel.basic_publish(exchange='', routing_key='letterbox', body=json_message)

    print(f"Sent message: {json_message}")

    connection.close()

enviar_mensaje()
enviar_mensaje()
enviar_mensaje()

