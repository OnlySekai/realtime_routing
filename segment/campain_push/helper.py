import datetime as dt
import json
from config import CAMPAIGN_KAFKA_TOPIC
from repositories.redis.connection import redis_client
from repositories.kafka.producer import producer_trigger
datetime = dt.datetime

def insert_user(msisdn, subs_package):
    redis_client.get_connection().set_start_subs(msisdn, subs_package)
    redis_client.get_connection().set_active_subs(msisdn, subs_package)


def get_subs_info(msisdn):
    return redis_client.get_connection().json().get("SubsInfo:" + msisdn)

def insert_push_log(msisdn, event_time, segment):
    key_today = "SubsCampaignPush:" + datetime.now().strftime('%Y-%m-%d')
    if redis_client.get_connection().exists(key_today):
        redis_client.get_connection().json().merge(key_today, '$.' + msisdn, {segment: event_time})
    else:
        redis_client.get_connection().json().set(key_today, '$', {msisdn: {segment: event_time}})

def pushCEP(msisdn, segment, trigger_time=None):
    event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expire_time = f"{(datetime.combine(datetime.now().date(), datetime.max.time()) - dt.timedelta(microseconds=1)).isoformat(timespec='milliseconds')}Z"
    producer_trigger.produce(
        CAMPAIGN_KAFKA_TOPIC,
        value=json.dumps(
            {
                "MSISDN": msisdn,
                "CMP_SEGMENT_ID": segment,
                "push_time": event_time,
                "expire_time": expire_time,
            }
        ),
    )
    producer_trigger.flush()
    print(
        f"Pushed CEP for {msisdn} with segment {segment} | {event_time} | {trigger_time}"
    )
    insert_push_log(msisdn, event_time, segment)

def set_first_subs_time(msisdn, event_time):
    if not redis_client.get_connection().exists("SubsInfo:" + msisdn):
        redis_client.get_connection().json().set("SubsInfo:" + msisdn, '$', {'firsSubsTime': event_time})
    else:
        redis_client.get_connection().json().set("SubsInfo:" + msisdn, '.firsSubsTime', event_time)

def update_subs_info(msisdn, lastPushSegment, activeSubs):
    pipe = redis_client.get_connection().pipeline()
    pipe.json().set("SubsInfo:" + msisdn, '.lastPushSegment', lastPushSegment)
    pipe.json().set("SubsInfo:" + msisdn, '.activeSubs', activeSubs)
    pipe.json().set("SubsInfo:" + msisdn, '.pushTimes', 0, nx=True)
    pipe.json().numincrby("SubsInfo:" + msisdn, '.pushTimes', 1)
    pipe.execute()

