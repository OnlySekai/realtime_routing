from datetime import timedelta
from repositories.redis.models.sub_info_v2 import get_subs_info, update_active_sub, update_predict_sub
from repositories.redis.models.sub_push_status import update_and_get_sub_push_status


def get_sub_status(msisdn):
    return get_subs_info(msisdn)


def update_push_status(msisdn, segment):
    return update_and_get_sub_push_status(msisdn, segment)

def update_sub_info(msisdn,sub, start_date, end_date):
    expire_time = end_date
    if (expire_time is None):
        expire_time = start_date + timedelta(days=30)
    if (expire_time < timedelta(days=0)):
        return None
    update_active_sub(msisdn, sub, expire_time)

def update_predict_sub_info(msisdn, sub, partition_date):
    expire_time = partition_date + timedelta(days=1)
    if (expire_time < timedelta(days=0)):
        return None
    return update_predict_sub(msisdn,sub, expire_time)
