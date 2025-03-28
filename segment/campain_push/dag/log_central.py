from repositories.kafka.consumer import consumer_logCentral
from segment.campain_push.log_operator import *

from lib.operator.simple import *
campain_log_flow = consumer_logCentral \
    .bind(wrap_filter(have_data)) \
    .bind(project_data) \
    .bind(join_sub_info) 

campain_seg1_flow = campain_log_flow \
    .fork() \
    .bind(wrap_filter_re(have_sub_info)) 

campain_old_flow = campain_log_flow \
    .fork() \
    .bind(wrap_filter(contidion_sub_times)) \
    .bind(wrap_filter(condition_first_time)) \
    
campain_seg4_flow = campain_old_flow \
    .fork() \
    .bind(wrap_filter(flow_4_condition)) \
    .bind(push_data)

campain_seg2356_flow = campain_old_flow \
    .fork() \
    .bind(wrap_filter(flow_2356_condition)) \
    .bind(push_data)