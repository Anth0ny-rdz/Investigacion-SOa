import pika
import smtplib
from email.mime.text import MIMEText

def send_email(body):
    # Configuración del correo
    sender_email = "juninielvillero@gmail.com"
    receiver_email = "anthor1999@gmail.com"
    #la password es del sender
    password = "ovzc dkbz divv kwfu"

    msg = MIMEText(body)
    msg['Subject'] = 'Mensaje de que si vale la wea de arquitectura'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Enviar correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    send_email(body.decode())

def start_consuming():
    # Conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola
    channel.queue_declare(queue='email_queue')

    # Configurar el consumidor
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Empezar a consumir mensajes
start_consuming()
