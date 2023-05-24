
## Parte 2 n-Threads para producir mensajes


## Ejecutar el archivo

Al ejecutar el archivo principal (main.py), se iniciarán dos hilos: uno para el receive.py y otro para el send.py . El consumidor estará escuchando y esperando mensajes en la cola de RabbitMQ, mientras que el productor (send) generará y enviará mensajes a la misma cola.

Tengo un problema, que cuando le pongo ctrl+c para detener la ejecución, no se detiene, y tengo que cerrar la terminal. No sé si es un problema de mi computadora o del código.// SOLUCIONADO

Ahora se tiene que presionar ctrl+c dos veces para detener la ejecución. Esto se debe a que se tienen dos hilos, y cada uno tiene su propio bucle infinito. Por lo tanto, se debe presionar ctrl+c dos veces para detener cada bucle.

Ademas, ahora se puede configurar el numero de hilos y el intervalo de tiempo del mismo que se quiera. Para esto, se debe modificar la variable `n_threads` y `delay` en el archivo `main.py`.

La carpeta _pycache_ es una carpeta creada por Python para almacenar archivos de caché compilados.
