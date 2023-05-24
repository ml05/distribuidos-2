# multiples threads (m-CONSUMERS)

## Ejecutar los archivos

Se deben ejecutar los archivos en terminales distintas, primero consumer.py y luego todos los producer.py que se deseen

```
python3 consumer.py <0>
python3 producer.py
...
```
Se deben ejecutar los archivos en terminales distintas, primero consumer.py (se debe colocar un id) y luego producer.py que se deseen
Preguntara por el numero de consumidores que se desean, si se desea un consumidor se debe ingresar 0, la cantidad
de mensajes que se desean enviar y el tiempo de espera entre mensajes.