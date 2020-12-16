try:
    import pika

except Exception as e:
    print("Some Modules are missing {}".format_map(e))


class MetaClass(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """ Singelton Design Pattern  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitmqConfigure(metaclass=MetaClass):

    def __init__(self, queue='hello', host='localhost', routingKey='hello',
                 exchange='', durable=False, delivery_mode=1):
        """ Configure Rabbit Mq Server  """
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange
        self.durable = durable
        self.delivery_mode = delivery_mode


class RabbitMq():

    def __init__(self, server):

        """
        :param server: Object of class RabbitmqConfigure
        """

        self.server = server
        self._channel = self.__connect(host=self.server.host)

    def __connect(self, host):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        return self._connection.channel()

    def declare_queue(self):

        data = {"queue": self.server.queue}
        if self.server.durable:
            data["durable"] = self.server.durable
        self._channel.queue_declare(**data)

    def publish(self, payload={}):

        """
        :param payload: JSON payload
        :return: None
        """
        self.declare_queue()

        if self.server.delivery_mode == 1:
            self._channel.basic_publish(exchange=self.server.exchange,
                                        routing_key=self.server.routingKey,
                                        body=str(payload))

        self._channel.basic_publish(exchange=self.server.exchange,
                                    routing_key=self.server.routingKey,
                                    body=str(payload),
                                    properties=pika.BasicProperties(
                                        delivery_mode=self.server.delivery_mode,
                                    )
                                    )
        print("Published Message: {}".format(payload))

    def close_conn(self):
        self._connection.close()
        print("Connection closed")
