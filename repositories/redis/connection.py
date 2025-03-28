from redis_om import get_redis_connection, JsonModel
from contansts.config import REDIS_HOST, REDIS_PORT, REDIS_DB

redis_client = get_redis_connection(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


class Model(JsonModel):
    class Meta:
        database = redis_client

    def save(self):
        return super().save()
    
    def update(self, updates: dict = None):
        for key, value in updates.items():
            redis_client.json().set(self.key(), f".{key}", value)

    @classmethod
    def get(cls, user_id: str):
        return cls.find(cls.user_id == user_id).first()
