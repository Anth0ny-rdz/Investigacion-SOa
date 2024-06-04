import pika

def send_message(message):
    # Conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola
    channel.queue_declare(queue='email_queue')

    # Enviar un mensaje a la cola
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f" [x] Sent '{message}'")

    # Cerrar la conexión
    connection.close()

# Ejemplo de envío de mensaje
send_message("Hello, this is a test message.")
