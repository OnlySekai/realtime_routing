from repositories.kafka.consumer import consumer_logCentral
from lib.operator.simple import wrap_filter,wrap_filter_re
from segment.marketing_sub.dag.helper import FilterState
from segment.marketing_sub.operator import *

Data = FilterState(consumer_logCentral
    .fork("Data")
    .bind(projected_data_trans)
    .bind(wrap_filter(is_data))
)

DataPlus = ( Data
    .fork("DataPlus")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment('Pluss data '))
)

DataPre = ( Data
    .fork("DataPre")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment('Pre data'))
)

Topup = FilterState(consumer_logCentral
    .fork("Topup")
    .bind(projected_topup_trans)
    .bind(wrap_filter(is_top_up))
)

TopupPlus = ( Topup
    .fork("TopupPlus")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment('Plus top up '))
)

TopupPre = ( Topup
    .fork("TopupPre")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment('Pre top up'))
)