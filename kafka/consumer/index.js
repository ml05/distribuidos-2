import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';

import fs from 'fs';
const filePath = './log-consumer.txt';

const consumerConfig = {
  'metadata.broker.list': 'localhost:9092',
};

function createConsumer(identificador) {
  const consumerGroup = new Kafka.KafkaConsumer({
    ...consumerConfig,
    'group.id': 'consumer-group-'+identificador.toString(),
  }, {}, { topic: 'test' });

  consumerGroup.connect();
  let message = '';
  consumerGroup.on('ready', () => {
    console.log('consumer ready..')
    consumerGroup.subscribe(['test']);
    consumerGroup.consume();
  }).on('data', function (data) {
    message = eventType.fromBuffer(data.value).toString();
    let tiempo = Date.now().toString();
    console.log(`consumer ` + identificador.toString() + ` received message: ${message}`);
    message = message + ' ' + tiempo + '\n';
    fs.writeFile(filePath, message, {'flag': 'a+'}, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log('File written successfully.');
      }
    });
  });
}

// establecer en 1 para probar con un solo consumidor
const numConsumers = 10;
// Crear consumidores en grupos diferentes
for (let i = 0; i < numConsumers; i++) {
  createConsumer(i);
}
