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
      type: { type: 'enum', symbols: ['DOG', 'CAT'] }
    },
    {
      name: 'noise',
      type: 'string'
    },
    {
      name: 'timestamp',
      type: 'string'
    }
  ]
});
