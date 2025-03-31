from confluent_kafka import Producer
from config import *

producer_trigger = Producer(KAFKA_137_BASED_CONSUMER_CONFIGS)
