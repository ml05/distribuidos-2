import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';

const consumerConfig = {
  'metadata.broker.list': 'localhost:9092',
};

function createConsumer(categoria) {
    let id = 0;
    if (categoria === 'humedad') {
        id = 1;
    } else if (categoria === 'temperatura') {
        id = 2;
    } else if (categoria === 'co2') {
        id = 3;
    } else if (categoria === 'luminosidad') {
        id = 4;
    } else if (categoria === 'ph') {
        id = 5;
    }


  const consumerGroup = new Kafka.KafkaConsumer({
    ...consumerConfig,
    'group.id': id,
  }, {}, { topic: categoria });

  consumerGroup.connect();

  consumerGroup.on('ready', () => {
    console.log('consumer ready..')
    consumerGroup.subscribe([categoria]);
    consumerGroup.consume();
  }).on('data', function (data) {
    console.log(`consumer ` + categoria + ` received message: ${eventType.fromBuffer(data.value)}`);
  });
}

// Crear consumidor para cada categoria
createConsumer('humedad');
createConsumer('temperatura');
createConsumer('co2');
createConsumer('luminosidad');
createConsumer('ph');
