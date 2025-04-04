from repositories.redis.connection import redis_client

model_name = "SubsInfo"

def get_subs_info(msisdn):
    pipe = redis_client.get_connection().pipeline()
    pipe.get(f"SubsInfo:{msisdn}:active_sub")
    pipe.get(f"SubsInfo:{msisdn}:predict_sub")
    active_sub, predict_sub = pipe.execute()
    return {
        "active_sub": active_sub,
        "predict_sub": predict_sub,
    }

def update_active_sub(msisdn, active_sub, pxat=None):
    key = f"SubsInfo:{msisdn}:active_sub"
    redis_client.get_connection().set(key, active_sub, pxat=pxat)

def update_predict_sub(msisdn, predict_sub, pxat=None):
    key = f"SubsInfo:{msisdn}:predict_sub"
    redis_client.get_connection().set(key, predict_sub, pxat=pxat)


