import pika
import json
import time
import string
import random

def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def genData(size):
    data = {
        'timestamp': time.time(),
        'value': {'data': generar_cadena_aleatoria(size)}
    }
    return data

def enviar_mensaje(categoria, n, t):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    for i in range(n):
        mensaje = json.dumps(genData(t))
        channel.basic_publish(exchange='topic_logs', routing_key=categoria, body=mensaje)
        print(f"Device {categoria} sending: {mensaje}")
        time.sleep(t)

    connection.close()

if __name__ == '__main__':
    try:
        categoria = input("Ingrese la categoría: ")
        message_count = int(input("Ingrese la cantidad de mensajes a enviar: "))
        sleep_time = int(input("Ingrese el tiempo de espera entre mensajes: "))

        enviar_mensaje(categoria, message_count, sleep_time)
    except KeyboardInterrupt:
        print(' Interrupted')
