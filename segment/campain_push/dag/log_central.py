from repositories.kafka.consumer import consumer_logCentral
from segment.campain_push.log_operator import *
from segment.campain_push.constants import *

from lib.operator.simple import *

campain_log_flow = (
    consumer_logCentral.bind(wrap_filter(filter_event))
    .bind(validate_and_project_data)
    .bind(project_request_content)
    .bind(join_sub_info)
)

campain_seg1_flow = (
    campain_log_flow.fork("Seg1 flow", "", True)
    .bind(wrap_filter_re(have_sub_info))
    .bind(set_segment(SEGMENTS[1]))
    .bind(update_first_subs_time)
    .bind(update_info)
    .bind(push_data)
)

campain_old_flow = (
    campain_log_flow.fork("Seg had sub info flow", "", True)
    .bind(wrap_filter(have_sub_info))
    .bind(wrap_filter(contidion_sub_times))
    .bind(wrap_filter(condition_first_time))
)

campain_seg4_flow = (
    campain_old_flow.fork("Seg4 flow", "", True)
    .bind(wrap_filter(flow_4_condition))
    .bind(set_segment(SEGMENTS[4]))
    .bind(update_info)
    .bind(push_data)
)

campain_seg2356_flow = (
    campain_old_flow.fork("seg2356 flow", "", True)
    .bind(wrap_filter(flow_2356_condition))
    .bind(set_segment_by_lastest)
    .bind(update_info)
    .bind(push_data)
)
