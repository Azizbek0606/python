from app.core.rq.config import get_connection

def callback(ch, method, properties, body):
    print(f" [__________] get {body}")

def subscribe():
    connection = get_connection()
    channel = connection.channel()
    queue_name = "hello"
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    subscribe() 