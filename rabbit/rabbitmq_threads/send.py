import argparse
import pika
import json
import time
import string
import random
import threading

def generar_cadena_aleatoria(N):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(N))
    return cadena_aleatoria

def enviar_mensaje(delay, stop_event):
    while not stop_event.is_set():
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

        time.sleep(delay)

def send_messages(n_threads, delay):
    stop_event = threading.Event()  # Evento para detener la ejecución

    threads = []
    for _ in range(n_threads):
        thread = threading.Thread(target=enviar_mensaje, args=(delay, stop_event))
        thread.start()
        threads.append(thread)

    # Esperar a que se presione Enter para detener la ejecución
    input("Presiona Enter para detener la ejecución...\n")
    stop_event.set()

    # Esperar a que todos los hilos finalicen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send messages with configurable threads and delay")
    parser.add_argument("--threads", type=int, default=3, help="Numero de threads(devices)")
    parser.add_argument("--delay", type=int, default=5, help="Delay")

    args = parser.parse_args()

    send_messages(args.threads, args.delay)

