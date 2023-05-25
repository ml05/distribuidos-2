import pika
import json
import time
import string
import random

def generar_cadena_aleatoria(N):
    # Genera una cadena aleatoria de longitud N utilizando letras, dígitos y signos de puntuación
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def enviar_mensaje(categoria):
    # Función para enviar un mensaje a través de RabbitMQ
    connection_parameters = pika.ConnectionParameters('localhost', blocked_connection_timeout=0.1)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # Crear el mensaje en el formato adecuado
    data = {
        "timestamp": time.time(),
        "value": {
            "data": generar_cadena_aleatoria(4)  # Generar una cadena aleatoria de longitud 4
        }
    }

    json_message = json.dumps(data)  # Convertir el mensaje a formato JSON

    channel.basic_publish(exchange='topic_logs', routing_key=categoria, body=json_message)

    print(f"Device {categoria} sent message: {json_message}")  # Imprimir el mensaje enviado

    connection.close()

def send_message_random_category(categorias):
    # Función para enviar un mensaje a una categoría aleatoria
    categoria = random.choice(categorias)
    enviar_mensaje(categoria)

if __name__ == "__main__":
    categorias = ['temperatura', 'humedad', 'pH', 'luminosidad', 'CO2']  # Lista de categorías

    contador = 0

    while True:
        contador += 1
        print(f"Mensaje enviado #{contador}")
        send_message_random_category(categorias)  # Enviar mensaje a una categoría aleatoria
        time.sleep(1)  # Esperar un segundo antes de enviar el siguiente mensaje
