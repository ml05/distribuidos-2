
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
    delay = 7  # Intervalo de tiempo en segundos

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


