import pika, json, time, string, random

def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def genData(size):
    data = {
        'timestamp' : time.time(),
        'value' : {'data' : generar_cadena_aleatoria(size)}
    }
    return data

def enviar_mensaje(id, n, t):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    for i in range(n):
        mensaje = json.dumps(genData(t))
        properties = pika.BasicProperties(headers={'sender': id})
        channel.basic_publish(exchange='', routing_key='hello', properties=properties, body=mensaje)
        print(f"Device {id} sending: {mensaje}")
        time.sleep(t)

    connection.close()

if __name__ == '__main__':
    try:
        consumer_count = int(input("Ingrese la cantidad de consumidores (m): "))
        message_count = int(input("Ingrese la cantidad de mensajes a enviar por cada consumidor: "))
        sleep_time = int(input("Ingrese el tiempo de espera entre mensajes: "))

        for i in range(consumer_count):
            enviar_mensaje(str(i), message_count, sleep_time)
    except KeyboardInterrupt:
        print(' Interrupted')
