import datetime as dt
import json
from config import CAMPAIGN_KAFKA_TOPIC
from repositories.kafka.producer import producer_trigger
from repositories.redis.models.campaign_push import *
from repositories.redis.models.sub_info import *

datetime = dt.datetime


def insert_user(msisdn, subs_package):
    update_sub_info_by_msisdn(
        msisdn,
        [
            {"path": ".startSubs", "value": subs_package},
            {"path": ".activeSubs", "value": subs_package},
        ],
    ).execute()


def set_start_subs(msisdn, subs_package):
    update_sub_info_by_msisdn(
        msisdn, [{"path": ".startSubs", "value": subs_package}]
    ).execute()


def set_active_subs(msisdn, subs_package):
    update_sub_info_by_msisdn(
        msisdn, [{"path": ".activeSubs", "value": subs_package}]
    ).execute()


def set_first_subs_time(msisdn, event_time):
    update_sub_info_by_msisdn(
        msisdn, [{"path": ".firsSubsTime", "value": event_time}]
    ).execute()


def update_subs_info(msisdn, lastPushSegment, activeSubs):
    updates = [
        {"path": ".lastPushSegment", "value": lastPushSegment},
        {"path": ".activeSubs", "value": activeSubs},
        {"path": ".pushTimes", "value": 0, "nx": True},
    ]
    incs = [{"path": ".pushTimes", "value": 1}]
    update_and_inc_sub_info_by_msisdn(msisdn, updates, incs).execute()


def insert_push_log(msisdn, event_time, segment):
    return insert_push_campaign_log("SubsCampaignPush", msisdn, event_time, segment)


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
