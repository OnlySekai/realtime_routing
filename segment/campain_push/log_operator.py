import datetime as dt
from segment.campain_push.helper import *
from segment.campain_push.constants import *

datetime = dt.datetime


def filter_event(event):
    return (
        event.get("transactionId") == LOG_CENTRAL_TRANSACTION_ID
        and event.get("applicationCode") == LOG_CENTRAL_APPLICATION_CODE
    )


def validate_and_project_data(event):
    data = {
        "msisdn": event.get("account", None),
        "event_time": datetime.fromtimestamp(
            int(event.get("eventTime")) / 1000
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "request_content": event.get("requestContent", None),
        "processing_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    if any(value is None for value in data.values()):
        return None
    return data


def project_request_content(event):
    is_renew = event.get("request_content").get("isRenew", None)
    subs_code = event.get("request_content").get("subCode", None)
    if subs_code in PLUS_SUB_CODE:
        event["subs_package"] = "PLUS"
    if subs_code in PREMIUM_SUB_CODE:
        event["subs_package"] = "PREMIUM"
    if event.get("subs_package") is None:
        return
    action = "GIA_HAN" if is_renew else "MUA_MOI"
    del event["request_content"]
    event["action"] = action
    return event


def join_sub_info(event):
    msisdn = event["msisdn"]
    subs_info = get_subs_info(msisdn)
    if subs_info is None:
        return event
    subs_info = {
        "push_times": subs_info.get("pushTimes", 0),
        "start_subs": subs_info.get("startSubs", None),
        "last_push_segment": subs_info.get("lastPushSegment", None),
    }
    event["subs_info"] = subs_info
    return event


def have_sub_info(event):
    return bool(event.get("subs_info", None))


def contidion_sub_times(event):
    return event["subs_info"]["push_times"] < 3


def condition_first_time(event):
    return datetime.now() - datetime.strptime(
        event["event_time"], "%Y-%m-%d %H:%M:%S"
    ) <= dt.timedelta(days=100)


def flow_4_condition(event):
    return (
        event["subs_info"]["start_subs"] == "PLUS"
        and event.get("subs_package", None) == "PREMIUM"
        and event.get("action", None) == "MUA_MOI"
        and event["subs_info"]["push_times"] == 0
    )
# check mua goi pre


def flow_2356_condition(event):
    return event["subs_info"]["push_times"] > 0


def set_segment(segment):
    def add_segment(event):
        event["segment"] = segment \
            if not isinstance(segment, dict) \
            else segment.get(event.get("subs_package"))
        return event
    return add_segment


def set_segment_by_lastest(event):
    last_push_segment = event.get("subs_info").get("last_push_segment")
    segment = None
    for key, value in SEGMENTS.items():
        if isinstance(value, dict):
            if last_push_segment in value.values():
                segment = SEGMENTS[int(key) + 1]
                break
        elif value == last_push_segment:
            segment = SEGMENTS[int(key) + 1]
            break
    if (segment is None):
        return None
    return set_segment(segment)(event)


def push_data(event):
    pushCEP(event["msisdn"], event["segment"])
    return event


def update_first_subs_time(event):
    set_first_subs_time(event["msisdn"], event["event_time"])
    return event


def update_info(event):
    update_subs_info(event["msisdn"], event["segment"], event["subs_package"])
    return event
