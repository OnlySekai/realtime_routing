from redis_om import get_redis_connection, JsonModel
from contansts.config import REDIS_HOST, REDIS_PORT, REDIS_DB

redis_client = get_redis_connection(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)