from segment.marketing_sub.dag.core_payment import (
    DataPlus,
    DataPre,
    TopupPlus,
    TopupPre,
)
from lib.utils import JoinPoint
from lib.operator.simple import wrap_filter
from segment.marketing_sub.operator import *

main = (
    JoinPoint(
        "Prepare Push",
        "",
        TopupPlus,
        TopupPre,
        DataPre,
        DataPlus,
    )
    .bind(update_and_join_push_total)
    .bind(wrap_filter(daily_push_condition))
    .bind(wrap_filter(weekly_push_condition))
    .bind(wrap_filter(weekly_push_segment_condition))
    .bind(push_data)
)
