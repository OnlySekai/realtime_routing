from repositories.kafka.consumer import consumer_hdfs
from segment.campain_push.hdfs_operator import *

from lib.operator.simple import *

campain_hdfs_flow = consumer_hdfs.bind(write_his_data)

