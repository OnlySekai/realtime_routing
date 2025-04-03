from lib.operator.simple import wrap_filter
from segment.marketing_sub.operator import *

FilterState = lambda state: (state
    .bind(wrap_filter(not_staff))
    .bind(join_predict)
    .bind(wrap_filter(in_predict))
    .bind(add_sub_status)
    .bind(wrap_filter(diff_predicted))
)