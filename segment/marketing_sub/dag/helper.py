from lib.operator.simple import wrap_filter, wrap_filter_re
from segment.marketing_sub.operator import *

FilterState = lambda state: (
    state.bind(add_sub_status)
    .bind(wrap_filter_re(is_active_sub_pre))
    .bind(wrap_filter(in_predict))
    .bind(wrap_filter(diff_predicted))
)
