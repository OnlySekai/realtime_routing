from repositories.redis.connection import redis_client

def insert_user(msisdn, subs_package):
    redis_client.set_start_subs(msisdn, subs_package)
    redis_client.set_active_subs(msisdn, subs_package)

def get_subs_info(msisdn):
    return redis_client.json().get("SubsInfo:" + msisdn)

def pushCEP(redis_client, producer, msisdn, segment, trigger_time=None):
    event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expire_time = f"{(datetime.combine(datetime.now().date(), datetime.max.time()) - timedelta(microseconds=1)).isoformat(seq='T', timespec='milliseconds')}Z"
    producer.produce(CAMPAIGN_KAFKA_TOPIC, value=json.dumps({'MSISDN': msisdn, 'CMP_SEGMENT_ID': segment, 'push_time': event_time, 'expire_time': expire_time}))
    producer.flush()
    print(f"Pushed CEP for {msisdn} with segment {segment} | {event_time} | {trigger_time}")
    redis_client.insert_push_log(msisdn, event_time, segment)