class State(State):
    def __init__(self):
        super().__init__()
        self.kafka_consumer = KafkaConsumer(
            bootstrap_servers=KAFKA_SERVER,
            group_id=KAFKA_GROUP_ID,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.kafka_consumer.subscribe([KAFKA_TOPIC])

    def run(self):
        super().run()
        for message in self.kafka_consumer:
            self.emit('message', message.value)