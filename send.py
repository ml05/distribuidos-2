import pika
import json
import time
import string
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

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
# en el futuro, este valor podria ser aleatorio o entregado por el usuario
mensaje = json.dumps(genData(10))

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=mensaje)



print(" [x] Sent %s" % mensaje)

connection.close()