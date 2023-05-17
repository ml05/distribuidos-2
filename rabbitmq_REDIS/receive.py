#!/usr/bin/env python
import pika, sys, os
import redis

def main():
    # conexion con REDIS
    redis_client = redis.Redis(host='localhost', port=6379, db=0) # puerto por defecto de REDIS

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        sender = properties.headers.get('sender')
        mensaje = body.decode('utf-8') # guardar mensajes a una variable para guardar en REDIS
        print("Device", sender, "sending:", body.decode('utf-8'))
        
        # guardar los datos en redis
        redis_client.rpush('mensajes', mensaje)

    channel.basic_consume(queue='hello', 
                          on_message_callback=callback, 
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)