try:
    import pika
except ModuleNotFoundError as err:
    # Error handling
    print(err)
import json


class RabbitManager:
    def __init__(self):
        self.connection = None
        self.channel = None

    def setup_conn(self, protocol, _url, un, pw):
        try:
            url = f'{protocol}://{un}:{pw}@{_url}'
            params = pika.URLParameters(url)
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='dask_task_status', durable=True)
        except Exception as e:
            print(e.__str__())

    def get_connection(self):
        return self.connection

    def get_channel(self):
        return self.channel

    def send_message(self, exchange: str, routing_key: str, message):
        try:
            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=json.dumps(message).encode('utf-8'),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
            print('RabbitMq Send Message Success')
        except Exception as e:
            print(e.__str__())
