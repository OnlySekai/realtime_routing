from repositories.redis.connection import redis_client
from datetime import datetime, timedelta


def update_and_get_sub_push_status(msisdn, segment):
    pipeline = redis_client.get_connection().pipeline()
    now = datetime.now()
    end_of_day = datetime.combine(now.date(), datetime.max.time())
    end_of_week = end_of_day + timedelta(days=(6 - now.weekday()))

    pipeline.incr(f"{msisdn}:daily:SubPushStatus:total", 1)
    pipeline.incr(f"{msisdn}:weekly:SubPushStatus:total", 1)
    pipeline.incr(f"{msisdn}:weekly:SubPushStatus:total:{segment}", 1)

    pipeline.expireat(f"{msisdn}:daily:SubPushStatus:total", end_of_day)
    pipeline.expireat(f"{msisdn}:weekly:SubPushStatus:total", end_of_week)
    pipeline.expireat(f"{msisdn}:weekly:SubPushStatus:total:{segment}", end_of_week)

    results = pipeline.execute()
    return {"daily": results[0], "weekly": results[1], "weekly_per_segment": results[2]}
