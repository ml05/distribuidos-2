from send import *
import threading

# enviar un mensaje cada t segundos
# se crearan n dispositivos que enviaran mensajes
def enviar(n, t):
    for i in range(n):
        # se crea un hilo para cada dispositivo
        # se le entrega un id y un tiempo
        t = threading.Thread(target=enviar_mensaje, args=(i, t))
        t.start()