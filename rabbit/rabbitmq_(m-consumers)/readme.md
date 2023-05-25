# Implementacion rabbitmq con multiples threads

## Punto 3 de la tarea: m-CONSUMERS

## Ejecutar los archivos

Se deben ejecutar los archivos en terminales distintas, primero consumer.py y luego todos los producer.py que se deseen

```
python3 consumer.py 1
python3 producer.py
...
```
Se deben ejecutar los archivos en terminales distintas, primero consumer.py (se debe colocar un id) y luego producer.py que se deseen
Preguntara por el numero de consumidores que se desean, si se desea un consumidor se debe ingresar 1, la cantidad
de mensajes que se desean enviar y el tiempo de espera entre mensajes.

En esta implementación, se utiliza RabbitMQ como intermediario de mensajes para permitir la comunicación entre múltiples productores y un consumidor. Los productores generan mensajes y los envían a RabbitMQ, mientras que el consumidor se suscribe a una cola específica para recibir y procesar los mensajes.

RabbitMQ actúa como un intermediario confiable y eficiente, asegurando que los mensajes enviados por los productores lleguen al consumidor. Esto permite implementar sistemas distribuidos, monitoreo, procesamiento de eventos en tiempo real y otros casos de uso.

En resumen, la implementación con RabbitMQ y múltiples productores permite una comunicación escalable y flexible entre componentes distribuidos, brindando robustez y confiabilidad a las aplicaciones y sistemas.