import datetime as dt
from repositories.redis.connection import redis_client
from repositories.redis.models.sub_info import *

datetime = dt.datetime


def insert_push_campaign_log(campaign, msisdn, event_time, segment):
    key_today = f"{campaign}:" + datetime.now().strftime("%Y-%m-%d")
    if redis_client.get_connection().exists(key_today):
        redis_client.get_connection().json().merge(
            key_today, "$." + msisdn, {segment: event_time}
        )
    else:
        redis_client.get_connection().json().set(
            key_today, "$", {msisdn: {segment: event_time}}
        )
