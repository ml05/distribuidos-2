ubucacion: cd rabbit\rabbitmq_multi_threads\categorias


# Implementacion rabbitmq con multiples threads

## Ejecutar los archivos
```
python3 consumer.py 1

python3 producer.py
```
Se debera colocar un id de categoria en el consumer.py

en el producer.py se preguntara la categoria (puede ser ['temperatura', 'humedad', 'pH', 'luminosidad', 'CO2']), la cantidad de mensajes a enviar y el tiempo de espera entre cada mensaje