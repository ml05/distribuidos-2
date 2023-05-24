import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';

const consumerConfig = {
  'metadata.broker.list': 'localhost:9092',
};

function createConsumer(identificador) {
  const consumerGroup = new Kafka.KafkaConsumer({
    ...consumerConfig,
    'group.id': 'consumer-group-'+identificador.toString(),
  }, {}, { topic: 'test' });

  consumerGroup.connect();

  consumerGroup.on('ready', () => {
    console.log('consumer ready..')
    consumerGroup.subscribe(['test']);
    consumerGroup.consume();
  }).on('data', function (data) {
    console.log(`consumer ` + identificador.toString() + ` received message: ${eventType.fromBuffer(data.value)}`);
  });
}

// establecer en 1 para probar con un solo consumidor
const numConsumers = 2;
// Crear consumidores en grupos diferentes
for (let i = 0; i < numConsumers; i++) {
  createConsumer(i);
}
