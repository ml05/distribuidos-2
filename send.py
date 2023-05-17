import pika
import json
import time
import string
import random
import threading

# establecer conexion con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# declarar la cola en la que se va a enviar el mensaje
channel.queue_declare(queue='hello')

# funcion para generar una cadena aleatoria de mensajes de largo N
def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

# genData genera info de largo segun argumento
# informacion a enviar en formato JSON
# enviar: timestamp, values (debe ser configurable)
def genData(size):
    
    data = {
        'timestamp' : time.time(),
        'value' : {'data' : generar_cadena_aleatoria(size)}
    }
    return data

# se genera un mensaje de largo 10
# TODO este valor podria ser aleatorio o entregado por el usuario
mensaje = json.dumps(genData(10))

# modifica el encabezado del mensaje
# agregando el nombre de quien lo envia
# TODO cambiar a un valor entregado por el usuario
properties = pika.BasicProperties(headers={'sender': 'remitente_1'})

# publicar el mensaje
channel.basic_publish(exchange='',
                      routing_key='hello',
                      properties=properties,
                      body=mensaje)



print(" [x] Sent %s" % mensaje)

connection.close()