# Tarea 2 Sistemas Distribuidos

# RabbitMQ

## Para ejecutar RabbitMQ

```
docker run -d --hostname my-rabbit --name rabbitTest -p 5672:5672 rabbitmq:3
```

## Librerias para python

Para usar RabbitMQ, se utiliza la libreria pika (recordar que version de pip/python se esta utilizando)

```
sudo apt install python3-pip
pip3 install pika --upgrade
```

## Para revisar la lista de colas y la cantidad de mensajes tienen, se puede usar el siguiente comando en la terminal del container de Docker:

```
rabbitmqctl list_queues
```

## Ejecutar los archivos

Se deben ejecutar los archivos en terminales distintas, primero receive.py y luego todos los send.py que se deseen

```
python3 receive.py
python3 send.py
...
```