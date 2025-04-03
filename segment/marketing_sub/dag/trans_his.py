from lib.operator.simple import wrap_filter, wrap_filter_re
from repositories.kafka.consumer import consumer_logCentral
from segment.marketing_sub.dag.helper import FilterState
from segment.marketing_sub.operator import *

TransMoneyState = FilterState(consumer_logCentral
    .fork("TransMoneyState")
    .bind(projected_data_trans)
    .bind(wrap_filter(is_trans_money))
    .bind(add_threasold)
)

GreaterThanThreasold = (TransMoneyState
    .fork("GreaterThanThreasold")
    .bind(wrap_filter(greater_than_threasold))
)

PlusGreater = ( GreaterThanThreasold
    .fork("PlusGreater")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment('Plus > 50'))
)

PreGreater = ( GreaterThanThreasold
    .fork("PreGreater")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment('Pre > 50'))
)

LessThanThreasold = (TransMoneyState
    .fork("LessThanThreasold")
    .bind(wrap_filter_re(greater_than_threasold))
)

PlusLess = ( LessThanThreasold
    .fork("PlusLess")
    .bind(wrap_filter(is_predicted_plus))
    .bind(set_segment('Pluss < '))
)

PreLess = ( LessThanThreasold
    .fork("PreLess")
    .bind(wrap_filter(is_predicted_pre))
    .bind(set_segment('Pre <'))
)