import datetime
from segment.campain_push.helper import *

PLUS_SUB_CODE = ['VTM1', 'VTM3']
PREMIUM_SUB_CODE = ['VTM2', 'VTM4']

have_data = lambda event: \
    event.get('msisdn') and \
    event.get('transaction_id') and \
    event.get('event_time') and \
    event.get('request_content') and \
    event.get('application_code')

project_data = lambda event: {
    k: event.get(k) \
        for k in ('msisdn', 'transaction_id', 'event_time', 'request_content', 'application_code') if event.get(k) is not None
}

def join_sub_info(event): 
     subs_info = get_subs_info(event.msisdn)
     event.subs_info = {
        k: subs_info.get(k) \
        for k in ('pushTimes', 'start_subs') if subs_info.get(k) is not None
        }
     return event

have_sub_info = lambda event: bool(event.subs_info)

contidion_sub_times = lambda event: event.subs_info.pushTimes < 3

def condition_first_time(event):
    event_time = datetime.fromtimestamp(int(event.eventTime) / 1000).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.now() - datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S') > datetime.timedelta(days=100)

flow_4_condition = lambda event: \
    event.subs_info['start_subs'] == 'PLUS' and \
    event.request_content.sub_code in PREMIUM_SUB_CODE and \
    event.action =='MUA_MOI' and \
    event.subs_info.pushTimes == 0
    # check mua goi pre

flow_2356_condition = lambda event: \
      event.subs_info.pushTimes != 0