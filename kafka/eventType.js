import avro from 'avsc';

export default avro.Type.forSchema({
  type: 'record',
  fields: [
    {
      name: 'id',
      type: 'string'
    },
    {
      name: 'category',
      type: { type: 'enum', symbols: ['Temperatura', 'Humedad', 'CO2', 'Luminosidad', 'pH'] }
    },
    {
      name: 'value',
      type: 'string'
    },
    {
      name: 'timestamp',
      type: 'string'
    }
  ]
});
