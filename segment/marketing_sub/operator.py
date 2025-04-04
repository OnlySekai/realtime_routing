from segment.marketing_sub.constants import MASTER_DATA, TOP_UP_SERVICES_CODE
from segment.marketing_sub.helper import get_sub_status, update_predict_sub_info, update_sub_info


def update_total_trans(event):
    return event


def update_push_status(event):
    update_push_status(event.get("msisdn"), event.get("segment"))
    return event


def push_data(event):
    return event


def projected_data_trans(event):
    return event


def project_topup_data(event):
    data = {
        "msisdn": event.get("identifyValue"),
        "service_code": event.get("content", {})
        .get("paymentDetails", [{}])[0]
        .get("serviceCode"),
        "master": event.get("content", {}).get("paymentDetails", [{}])[0].get("master"),
    }
    if not (data.get("msisdn") and data.get("service_code")):
        return None
    return data


def is_data(event):
    return event.get("master") in MASTER_DATA


def is_predicted_plus(event):
    return event.get("sub_status", {}).get("predict_sub") == "PLUS"


def set_segment(segment_name):
    def set_segment(event):
        event.segment = segment_name
        return event

    return set_segment


def is_predicted_pre(event):
    return event.get("sub_status", {}).get("predict_sub") == "PREMIUM"


def is_top_up(event):
    return event.get("services_code", None) in TOP_UP_SERVICES_CODE


def is_trans_money(event):
    return event


def add_threasold(event):
    return event


def greater_than_threasold(event):
    return event


def add_sub_status(event):
    event["sub_status"] = get_sub_status(event.get("msisdn"))
    return event


def in_predict(event):
    return event.get("sub_status", {}).get("predict_sub") is not None

def is_active_sub_pre(event):
    return event.get("sub_status", {}).get("active_sub") == "PREMIUM"


def diff_predicted(event):
    sub_status = event.get("sub_status", {})
    return sub_status.get("predict_sub") != event.get("active_sub")


def update_and_join_push_total(event):
    event["push_status"] = update_push_status(event.get("msisdn"), event.get("segment"))
    return event


def daily_push_condition(event):
    return event.get("push_status", {}).get("daily", 0) <= 1


def weekly_push_condition(event):
    return event.get("push_status", {}).get("weekly", 0) <= 3


def weekly_push_segment_condition(event):
    return event.get("push_status", {}).get("weekly_per_segment", 0) <= 2

def update_sub_status(event):
    update_sub_info(
        event.get("msisdn"),
        event.get("active_sub"),
        event.get("start_date"),
        event.get("end_date"),
    )
    return event

def update_predict(event):
    update_predict_sub_info(
        event.get("msisdn"),
        event.get("predict_sub"),
        event.get("partition_date"),
    )
    return event

def is_update_predict(event):
    return event.get("service") == "update_predict_sub"

def is_update_active_sub(event):
    return event.get("service") == "update_active_sub"
