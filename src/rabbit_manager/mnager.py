try:
    import pika
except ModuleNotFoundError as err:
    # Error handling
    print(err)
import json


def setup_conn(protocol, _url, un, pw):
    try:
        url = f'{protocol}://{un}:{pw}@{_url}'
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='dask_task_status', durable=True)
        return channel
    except Exception as e:
        print(e.__str__())
        return None


def send_message(channel, exchange: str, routing_key: str, message: bytes):
    try:
        channel.basic_publish(
            exchange='',
            routing_key='dask_task_status',
            body=json.dumps(message).encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print('Success')
    except Exception as e:
        print(e.__str__())
