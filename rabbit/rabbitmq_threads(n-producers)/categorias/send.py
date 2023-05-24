import pika
import json
import time
import string
import random
import threading

def generar_cadena_aleatoria(N):
    # Genera una cadena aleatoria de longitud N utilizando letras, dígitos y signos de puntuación
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def enviar_mensaje(categoria, delay, stop_event):
    # Función para enviar mensajes a través de RabbitMQ
    while not stop_event.is_set():  # Continuar hasta que se establezca el evento de detener
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

        time.sleep(delay)  # Esperar un tiempo antes de enviar el siguiente mensaje

def send_messages(categorias, delay):
    # Función para enviar mensajes para cada categoría en hilos separados
    stop_event = threading.Event()  # Evento para detener la ejecución

    threads = []
    for categoria in categorias:
        thread = threading.Thread(target=enviar_mensaje, args=(categoria, delay, stop_event))
        thread.start()
        threads.append(thread)

    input("Presiona Enter para detener la ejecución...\n")  # Esperar a que se presione Enter para detener la ejecución
    stop_event.set()  # Establecer el evento para detener la ejecución en los hilos

    for thread in threads:
        thread.join()  # Esperar a que todos los hilos finalicen

if __name__ == "__main__":
    categorias = ['temperatura', 'humedad', 'pH', 'luminosidad', 'CO2']  # Lista de categorías
    delay = 5  # Retardo entre mensajes

    send_messages(categorias, delay)  # Llamar a la función para enviar los mensajes
