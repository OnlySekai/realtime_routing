from repositories.kafka.consumer import consumer_history_service_insert_hbase_object
from lib.operator.simple import wrap_filter, wrap_filter_re
from segment.marketing_sub.dag.helper import FilterState
from segment.marketing_sub.operator import *
from segment.marketing_sub.constants import SEGMENT_TOPIC

DataTopup = (consumer_history_service_insert_hbase_object
             .fork("DataTopup", "", True)
             .bind(project_topup_data)
)

Data = FilterState(
    DataTopup
    .fork("Data", "", True)
    .bind(wrap_filter(is_data))
)

DataPlus = (
    Data.fork("DataPlus", "", True)
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment(SEGMENT_TOPIC["DATA_PLUS"]))
)

DataPre = (
    Data.fork("DataPre", "", True)
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment(SEGMENT_TOPIC["DATA_PREMIER"]))
)

Topup = FilterState(
    DataTopup
    .fork("Topup", "", True)
    .bind(wrap_filter(is_top_up))
)

TopupPlus = (
    Topup.fork("TopupPlus", "", True)
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment(SEGMENT_TOPIC["TOPUP_PLUS"]))
)

TopupPre = (
    Topup.fork("TopupPre", "", True)
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment(SEGMENT_TOPIC["TOPUP_PREMIER"]))
)
