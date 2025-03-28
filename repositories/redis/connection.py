import redis

from contansts.config import REDIS_DB, REDIS_HOST, REDIS_PORT
class RedisUtils(redis.StrictRedis):
    def __init__(self, config):
        self.redis_client = redis.StrictRedis(host=config['host'], port=config['port'], db=config['db'])

redis_client = RedisUtils({"host": REDIS_HOST, "port": REDIS_PORT, "db": REDIS_DB})