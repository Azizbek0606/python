from app.core.rq.config import get_connection

def publish():
    connection = get_connection()
    chanel = connection.channel()
    queue_name = "hello"
    chanel.queue_declare(queue=queue_name)
    for i in range(10):
        chanel.basic_publish(exchange='', routing_key=hello, body=f'Hello World {i}')
        print(f" [x] Sent 'Hello World {i}'")

if __name__ == "__main__":
    publish()
