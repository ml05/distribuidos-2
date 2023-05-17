
# RabbitMQ + REDIS cache

## descargar libreria REDIS para python

```
pip install redis
```

NOTAS:
En teoria no sirve ya que se supone que todos los datos que manda el IoT son diferentes, pero se hace util en la parte de separar las categorias, es decir, se puede guardar que X dispositivo es un refrigerador y eso mandarlo a un lugar predefinido sin tener que "identificar" de nuevo el dispositivo, eso solucionaria en teoria la problematica de enviar por diferentes vias a 1 solo brocker
