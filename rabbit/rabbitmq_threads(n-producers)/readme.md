
## Parte 2 n-Threads para producir mensajes


## Ejecutar el archivo

Ahora se puede configurar el numero de hilos y el intervalo de tiempo del mismo que se quiera. Para esto, se debe modificar la variable `n_threads` y `delay` en el archivo `send.py`.


## Ejecutar los archivos por separado y configurar manualmente threads y delay, por defecto vienen threads 3 y delay 5
```
python receive.py
python send.py --threads 3 --delay 5 // python send.py (ambas sirven)
```

a grandes rasgos, estos dos códigos se utilizan para implementar la comunicación de mensajes entre productores (emisores) y consumidores (receptores) utilizando RabbitMQ como intermediario.

El código del receptor (consumer) establece una conexión con RabbitMQ, declara una cola llamada "letterbox" y configura un consumidor en esa cola. Cuando se recibe un mensaje en la cola, se ejecuta la función on_message_received, que simplemente imprime el contenido del mensaje en la consola. El receptor continuamente consume mensajes en un bucle hasta que se interrumpe.

El código del emisor (producer) también establece una conexión con RabbitMQ y declara la misma cola "letterbox" en la que se enviarán los mensajes. Luego, se crea una función llamada enviar_mensaje que se ejecuta en un bucle hasta que se recibe una señal de parada. Dentro de esta función, se genera un mensaje en formato JSON con un timestamp y un valor que contiene una cadena aleatoria. El mensaje se publica en RabbitMQ y se imprime en la consola. El emisor puede enviar múltiples mensajes en paralelo utilizando hilos configurables, por defecto vienen threads 3 y delay 5 y en el codigo se puede modificar (linea 59 y 60).
