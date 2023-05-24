import pika
import json
import time
import string
import random

# Función para generar una cadena aleatoria de longitud N
def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

# Genera los datos del mensaje en formato JSON
def genData(size, categoria):
    data = {
        'category': categoria,
        'timestamp': time.time(),
        'value': {'data': generar_cadena_aleatoria(size)}
    }
    return data

# Función para enviar mensajes
# n es el identificador del remitente, 
# t es el tamaño de los datos
# cantidad es la cantidad de mensajes a enviar
# Los mensajes se envían a diferentes categorías
def enviar_mensaje(id, n, t, cantidad):
    # Establece la conexión con el servidor RabbitMQ
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    # Declara el exchange como topic
    channel.exchange_declare(exchange='sensor_data', exchange_type='topic')

    # Lista de categorías
    categorias = ['temperatura', 'humedad', 'pH', 'luminosidad', 'CO2']

    for _ in range(cantidad):
        # Elige una categoría aleatoria
        categoria = random.choice(categorias)
        # Genera los datos del mensaje
        mensaje = json.dumps(genData(n, categoria))
        # Crea las propiedades del mensaje con el identificador del remitente
        properties = pika.BasicProperties(headers={'sender': id})
        # Publica el mensaje en el exchange con la clave de enrutamiento correspondiente a la categoría
        channel.basic_publish(exchange='sensor_data', routing_key=categoria, properties=properties, body=mensaje)
        print(f"[x] Sent ({categoria}): {mensaje}")
        time.sleep(t)

    # Cierra la conexión
    connection.close()

# Envío de 5 mensajes aleatorios a diferentes categorías
enviar_mensaje("1", 4, 3, 7)
