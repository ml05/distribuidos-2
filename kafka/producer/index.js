import Kafka from 'node-rdkafka';
import eventType from '../eventType.js';

function createProducer(identificador){
  const stream = Kafka.Producer.createWriteStream({
  'metadata.broker.list': 'localhost:9092'
  }, {}, {
    topic: 'test'
  });

  stream.on('error', (err) => {
    console.error('Error in our kafka stream');
    console.error(err);
  });

  function queueRandomMessage() {
    const id = identificador.toString();
    const category = getRandomAnimal();
    const noise = getRandomNoise(category);
    const timestamp = Date.now().toString();
    const event = { id, category, noise, timestamp };
    const success = stream.write(eventType.toBuffer(event));     
    if (success) {
      console.log(`message queued (${JSON.stringify(event)})`);
    } else {
      console.log('Too many messages in the queue already..');
    }
  }

  function getRandomAnimal() {
    // aumentar categorias a cinco
    const categories = ['CAT', 'DOG'];
    return categories[Math.floor(Math.random() * categories.length)];
  }

  function getRandomNoise(animal) {
    if (animal === 'CAT') {
      const noises = ['meow', 'purr'];
      return noises[Math.floor(Math.random() * noises.length)];
    } else if (animal === 'DOG') {
      const noises = ['bark', 'woof'];
      return noises[Math.floor(Math.random() * noises.length)];
    } else {
      return 'silence..';
    }
  }

  setInterval(() => {
    queueRandomMessage();
  }, 3000);
}

// establecer cantidad de productores igual a 1 para tener solo un productor
const numProducers = 1;
// Crear múltiples productores
for (let i = 0; i < numProducers; i++) {
  createProducer(i);
}