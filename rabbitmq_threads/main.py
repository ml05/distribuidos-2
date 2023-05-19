import threading
import receive
import send

def main():
    # el consumidor tiene que ser uno solo y funcionar en su archivo aparte
    # Crear hilo para el consumidor
    consumer_thread = threading.Thread(target=receive.receive_messages)

    # Iniciar el hilo del consumidor
    consumer_thread.start()

    # se deben crear n threads (configurable)
    # se debe tener un delta tiempo configurable
    # Ejecutar el productor
    send.enviar_mensaje("1", 4, 3)

    # Esperar a que ambos hilos finalicen
    consumer_thread.join()

    # Cierre de la conexión (automáticamente manejado en send.py)

if __name__ == '__main__':
    main()
