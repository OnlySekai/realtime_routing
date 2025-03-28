from lib.kafka_consumer import KafkaSink
from operator.sample import trans1, trans2, trans3

Sink = KafkaSink().bind(trans1).bind(trans2).checkpoint()
Source1 = Sink.bind(trans3).bind(trans3).checkpoint()
Source2 = Sink.bind(trans3).bind(trans3).checkpoint()