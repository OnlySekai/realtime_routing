from lib.state.kafka_sink import KafkaSink
from config import *

consumer_logCentral = KafkaSink(
    LOG_CENTRAL_KAFKA_TOPIC, LOG_CENTRAL_KAFKA_CONSUMER_CONFIGS
)
consumer_history_service_insert_hbase_object = KafkaSink(
    HISTORY_SERVICE_INSERT_HBASE_OBJECT_TOPIC, HISTORY_SERVICE_INSERT_HBASE_OBJECT_KAFKA_CONSUMER_CONFIGS
)
consumer_hdfs = KafkaSink(HDFS_BATCH_TOPIC, KAFKA_137_BASED_CONSUMER_CONFIGS)
