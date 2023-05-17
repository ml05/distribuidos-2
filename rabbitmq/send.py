import pika, json, time, string, random


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

# enviar_mensaje envia un mensaje a la cola
# id: identificador del dispositivo
# n: tamano del mensajes a enviar
# t: tiempo entre mensajes
def enviar_mensaje(id, n, t):
    for i in range(3):
        mensaje = json.dumps(genData(n))
        # se crea un objeto BasicProperties para definir un header
        properties = pika.BasicProperties(headers={'sender': id})
        # publicar el mensaje
        channel.basic_publish(exchange='',
                            routing_key='hello',
                            properties=properties,
                            body=mensaje)
        # mensaje de confirmacion
        print(" [x] Sent %s" % mensaje)
        time.sleep(t)

enviar_mensaje("1", 4, 3)

connection.close()