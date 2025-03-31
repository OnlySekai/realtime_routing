from confluent_kafka import Consumer, TopicPartition


class KafkaConfluentConsumerUtiles:
    def __init__(self, topic, config, num_partitions=3):
        self.consumer = Consumer(config)
        self.topics = [topic]
        self.consumer.subscribe([topic])
        print("Topic:", self.consumer.assignment())
        self.consumer.assign(
            [TopicPartition(topic, partition=x) for x in range(num_partitions)]
        )
        print("Topic:", self.consumer.assignment())
