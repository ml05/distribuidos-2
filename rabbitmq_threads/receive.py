import pika

def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    messages_received = 0  # Contador de mensajes recibidos

    def callback(ch, method, properties, body):
        nonlocal messages_received  # Acceder a la variable messages_received en el ámbito superior
        sender = properties.headers.get('sender')
        print("Device", sender, "sending:", body.decode('utf-8'))

        messages_received += 1  # Incrementar el contador de mensajes recibidos

        if messages_received >= 6:  # Cambiar el número 6 por el número deseado de mensajes
            channel.stop_consuming()  # Detener la consumición de mensajes

    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()

receive_messages()