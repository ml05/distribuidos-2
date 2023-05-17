import threading
import receive
import send

def main():
    # Crear hilo para el consumidor
    consumer_thread = threading.Thread(target=receive.receive_messages)

    # Iniciar el hilo del consumidor
    consumer_thread.start()

    # Ejecutar el productor
    send.enviar_mensaje("1", 4, 3)

    # Esperar a que ambos hilos finalicen
    consumer_thread.join()

    # Cierre de la conexión (automáticamente manejado en send.py)

if __name__ == '__main__':
    main()
