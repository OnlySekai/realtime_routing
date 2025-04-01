from repositories.redis.connection import redis_client


def get_subs_info(msisdn):
    return redis_client.get_connection().json().get("SubsInfo:" + msisdn)


def update_sub_info_by_msisdn(msisdn, updates):
    key = "SubsInfo:" + msisdn
    pipe = redis_client.get_connection().pipeline()
    pipe.json().set(key, "$", {}, True)
    redis_client.pipe_set(pipe, key, updates)
    return pipe


def update_and_inc_sub_info_by_msisdn(msisdn, updates, incs):
    pipe = update_sub_info_by_msisdn(msisdn, updates)
    redis_client.pipe_inc(pipe, "SubsInfo:" + msisdn, incs)
    return pipe
