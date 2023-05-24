
## Categorias


## Ejecución
se deberan ejecutar los 5 receive en distintas terminales, ya que son las 5 categorias ('temperatura', 'humedad', 'pH', 'luminosidad', 'CO2') y luego el send en otra terminal, se puede ver como los mensajes se distribuyen entre los 5 receive y se imprimen en la consola.

```
python receive_temperatura.py
python receive_humedad.py
python receive_ph.py
python receive_luminosidad.py
python receive_co2.py
---------------------
python send.py
```

En esta implementación, tenemos un emisor (send) y 5 receptores (receive) de mensajes que se comunican a través de RabbitMQ utilizando categorías y topics.

El emisor (send) es responsable de enviar mensajes a RabbitMQ. Genera mensajes aleatorios con una categoría asociada y los publica en un exchange llamado "topic_logs" utilizando una routing_key que coincide con la categoría del mensaje. Cada mensaje está en formato JSON y contiene un timestamp y un valor de datos generados aleatoriamente.

El receptor (receive) está diseñado para recibir mensajes de una categoría específica. Se conecta a RabbitMQ, declara el exchange "topic_logs" y crea una cola exclusiva y anónima. Luego, se vincula la cola al exchange utilizando una routing_key correspondiente a la categoría deseada. A continuación, se configura un consumidor en la cola para recibir mensajes. Cuando se recibe un mensaje, se muestra en la consola junto con la categoría del dispositivo.