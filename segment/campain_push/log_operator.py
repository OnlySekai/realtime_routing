import datetime
from segment.campain_push.helper import *
from segment.campain_push.constants import *

def filter_event(event):
    return event.get("transactionId") == LOG_CENTRAL_TRANSACTION_ID and event.get("applicationCode") == LOG_CENTRAL_APPLICATION_CODE

def validate_and_project_data(event):
    data = {
            "msisdn": event.get("account", None),
            "event_time":datetime.fromtimestamp(int(event.get('eventTime')) / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            "request_content":event.get('requestContent', None),
            'processing_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    if any(value is None for value in data.values()):
        return None
    return data

def project_request_content(event):
    is_renew = event.get('request_content').get('isRenew', None)
    subs_code = event.get('request_content').get('subCode', None)
    if subs_code in PLUS_SUB_CODE:
        subs_package = 'PLUS'
    if subs_code in PREMIUM_SUB_CODE:
        subs_package = 'PREMIUM'
    action = 'GIA_HAN' if is_renew else 'MUA_MOI'
    del event['request_content']
    event['subs_package'] = subs_package
    event['action'] = action
    return event

def join_sub_info(event):
    subs_info = get_subs_info(event.msisdn)
    subs_info = {
        'push_times': subs_info.get("pushTimes", None),
        'start_subs': subs_info.get("startSubs", None)
    }
    event['subs_info'] = subs_info
    return event


have_sub_info = lambda event: bool(event['subs_info'])

contidion_sub_times = lambda event: event['subs_info']['push_times'] < 3


condition_first_time = lambda event: datetime.now() - datetime.strptime(event['event_time'], "%Y-%m-%d %H:%M:%S") <= datetime.timedelta(days=100)

flow_4_condition = (
    lambda event: event['subs_info']["start_subs"] == "PLUS"
    and event['request_content']['sub_code'] in PREMIUM_SUB_CODE
    and event['action'] == "MUA_MOI"
    and event['subs_info']['push_times'] == 0
)
# check mua goi pre

flow_2356_condition = lambda event: event['subs_info']['push_times'] > 0

def set_segment(segment):
    def add_segment(event):
        event['segment'] = segment
        return event
    return add_segment

def set_segment_by_lastest(event):
    last_push_segment = event.get('last_push_segment')
    if last_push_segment not in SEGMENTS.values():
        return None
    for key, value in SEGMENTS.items():
        if value == last_push_segment:
            event['segment'] = SEGMENTS[int(key) + 1]
            break
    return event

def push_data(event):
    pushCEP(event['msisdn'], event['segment'])
    return event

def update_first_subs_time(event):
    set_first_subs_time(event['msisdn'], event['event_time'])
    return event

def update_info(event):
    update_subs_info(event['msisdn'], event['segment'], event['subs_package'])
    return event
