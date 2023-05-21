'''import threading
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
    main()'''
import threading
import subprocess
import time

def send_messages(delay, stop_event):
    while not stop_event.is_set():
        subprocess.run(["python", "send.py"])
        time.sleep(delay)

if __name__ == "__main__":
    receive_thread = threading.Thread(target=lambda: subprocess.run(["python", "receive.py"]))
    receive_thread.start()

    # Configuración de hilos y tiempo
    n_threads = 3  # Número de hilos (dispositivos IoT)
    delay = 5  # Intervalo de tiempo en segundos

    threads = []
    stop_event = threading.Event()  # Evento de parada

    for i in range(n_threads):
        thread = threading.Thread(target=lambda: send_messages(delay, stop_event))
        threads.append(thread)
        thread.start()

    try:
        # Esperar a que un evento externo solicite detener la ejecución
        input("Presiona Enter para detener la ejecución...\n")
        stop_event.set()

        # Esperar a que todos los hilos finalicen
        receive_thread.join()
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        # Capturar la excepción "KeyboardInterrupt" y detener la ejecución de manera controlada
        stop_event.set()


