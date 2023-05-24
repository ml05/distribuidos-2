
# RabbitMQ + REDIS cache

## descargar libreria REDIS para python

```
pip install redis
```

## Contenedores requeridos
```
docker run -d --hostname my-rabbit --name rabbitTest -p 5672:5672 rabbitmq:3
docker run --name redis -p 6379:6379 -d redis
```

Para el punto 6 se utilizara RabbitMQ para agregar REDIS y ver el impacto que genera esto en comparacion a RabbitMQ sin REDIS y Kafka

Para que funcione correctamente esta parte se siguen las instrucciones de rabbitMQ pero utilizando los consumer modificados que se encuentran en esta carpeta (se reutilizan los producer originales).
