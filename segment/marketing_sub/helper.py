from repositories.redis.models.sub_info import get_subs_info
from repositories.redis.models.sub_push_status import update_and_get_sub_push_status


def get_sub_status(msisdn):
    return get_subs_info(msisdn)


def update_push_status(msisdn, segment):
    return update_and_get_sub_push_status(msisdn, segment)
