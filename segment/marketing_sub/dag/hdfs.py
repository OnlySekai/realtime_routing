from repositories.kafka.consumer import consumer_hdfs
from segment.marketing_sub.operator import *

from lib.operator.simple import *

predict_flow = consumer_hdfs.fork("campain_hdfs_flow", "", True).bind(wrap_filter(is_update_predict)).bind(update_predict)
active_flow = consumer_hdfs.fork("campain_hdfs_flow", "", True).bind(wrap_filter(is_update_active_sub)).bind(update_predict)
