import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';

function createProducer(identificador){
  function queueRandomMessage() {
    const id = identificador.toString();
    const category = getRandomCategory();
    const value = getRandomValue(category);
    const timestamp = Date.now().toString();
    const event = { id, category, value, timestamp };
    const success = stream.write(eventType.toBuffer(event));
    if (success) {
      console.log(`message queued (${JSON.stringify(event)})`);
    } else {
      console.log('Too many messages in the queue already..');
    }
  }

  const stream = Kafka.Producer.createWriteStream({
  'metadata.broker.list': 'localhost:9092'
  }, {}, {
    topic: 'test'
  });

  stream.on('error', (err) => {
    console.error('Error in our kafka stream');
    console.error(err);
  });

  function getRandomCategory() {
    const categories = ['Temperatura', 'Humedad', 'CO2', 'Luminosidad', 'pH'];
    return categories[Math.floor(Math.random() * categories.length)];
  }

  function getRandomValue(category) {
    if (category === 'Temperatura') {
      // temperatura dentro del intervalo 4-30 grados
      const random = Math.random();
      const range = 27;
      const value = Math.floor(random * range) + 4;
      return value.toString();
    } else if (category === 'Humedad') {
      // humedad dentro del intervalo 50-70%
      const random = Math.random();
      const range = 21;
      const value = Math.floor(random * range) + 50;
      return value.toString();
    } else if (category === 'CO2') {
      // intervalo dentro de 1000 y 1500 partes por millon (ppm)
      const random = Math.random();
      const range = 501;
      const value = Math.floor(random * range) + 1000;
      return value.toString();
    } else if (category === 'Luminosidad') {
      // intervalo de 100 y 1000 lux o micromoles de fotones por metro cuadrado por segundo
      const random = Math.random();
      const range = 901;
      const value = Math.floor(random * range) + 100;
      return value.toString();
    } else if (category === 'pH') {
      // dentro del intervalo de 5.5 a 7.5
      const random = Math.random();
      const range = 3;
      const value = Math.floor(random * range) + 5.5;
      return value.toString();
    } else {
      return 'no data';
    }
  }

    // modificar 1000 por la cantidad de milisegundos
  setInterval((t) => {
    queueRandomMessage();
  }, 1000);
}

// establecer cantidad de productores igual a 1 para tener solo un productor
const numProducers = 1;
// Crear múltiples productores
for (let i = 0; i < numProducers; i++) {
  createProducer(i);
}