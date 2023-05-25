* `npm install` - instala las dependencias.
* `./scripts/start-kafka.sh` - empieza kafka en el container.
* `./scripts/create-topic.sh` - configura kafka.
* `npm run start:producer` - inicia el IoT simulado.
* `npm run start:consumer` - inicia server.

NOTA, hay que cambiar el metodo de envio de informacion utilizado a Json ya que se pide en la tarea, este cliente/servidor ya tiene categorias, hay que "miniaturizarlo" para tener la base (yo me puedo encargar al rato atte Shun) aqui esta el video explicativo https://www.youtube.com/watch?v=EiDLKECLcZw&ab_channel=KrisFoster


# Instrucciones de uso

## Ejecutar el container para Kafka

Para esto, se utiliza el archivo 'docker-compose.yml' (tarda un tiempo)

```
docker-compose up
```

## Definir un topic 

Se puede usar el script 'create-topic.sh' o el siguiente codigo, en otra terminal:

```
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test
&& \
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic humedad
&& \
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic temperatura
&& \
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic co2
&& \
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic luminosidad
&& \
docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic ph
```

El topico creado se llamara 'test'

