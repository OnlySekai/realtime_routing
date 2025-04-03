from repositories.kafka.consumer import consumer_logCentral
from lib.operator.simple import wrap_filter, wrap_filter_re
from segment.marketing_sub.dag.helper import FilterState
from segment.marketing_sub.operator import *
from segment.marketing_sub.constants import SEGMENT_TOPIC

Data = FilterState(
    consumer_logCentral.fork("Data").bind(project_topup_data).bind(wrap_filter(is_data))
)

DataPlus = (
    Data.fork("DataPlus")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment(SEGMENT_TOPIC["DATA_PLUS"]))
)

DataPre = (
    Data.fork("DataPre")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment(SEGMENT_TOPIC["DATA_PREMIER"]))
)

Topup = FilterState(
    consumer_logCentral.fork("Topup")
    .bind(project_topup_data)
    .bind(wrap_filter(is_top_up))
)

TopupPlus = (
    Topup.fork("TopupPlus")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment(SEGMENT_TOPIC["TOPUP_PLUS"]))
)

TopupPre = (
    Topup.fork("TopupPre")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment(SEGMENT_TOPIC["TOPUP_PREMIER"]))
)
