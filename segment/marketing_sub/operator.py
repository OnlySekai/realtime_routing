def update_push_status(event):
    return event

def push_data(event):
    return event

def projected_data_trans(event): 
    return event
def project_topup_data(event):
    data = {
        "msisdn": event.get("identifyValue"),
        "service_code": event.get("content", {}).get("paymentDetails", [{}])[0].get("serviceCode"),
        "master": event.get("content", {}).get("paymentDetails", [{}])[0].get("master"),
    }
    if not ( data.get("msisdn") and data.get("service_code")):
        return None
    return data

def is_data(event):
    return event.master == "DATAVT"

def is_predicted_plus(event):
    return event['sub_status']['predict'] == 'PLUS'

def set_segment(segment_name):
    def set_segment(event):
        event.segment = segment_name
        return event
    return set_segment

def is_predicted_pre(event):
        return event['sub_status']['predict'] == 'PREMIRE'

def is_top_up(event):
    return event

def is_trans_money(event):
    return event

def add_threasold(event):
    return event

def greater_than_threasold(event):
    return event

def add_sub_status(event):
    event['sub_status'] = get_sub_status(event.msisdn)
    return event

def in_predict(event):
    return event['sub_status']['predict'] is not None

def diff_predicted(event):
    sub_status =  event['sub_status']
    return sub_status['predict'] != event['status']
