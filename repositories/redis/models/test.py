import redis
from redis_om import get_redis_connection, Field
from redis_om import JsonModel


class UserTest(JsonModel):
    user_id: str = Field(index=True)
    name: str
    age: int

    class Meta:
        database = get_redis_connection(
            host="localhost", port=6379, decode_responses=True
        )

    def save(self, updates: dict = None):
        if updates:
            redis_client = redis.Redis(
                host="localhost", port=6379, decode_responses=True
            )
            for key, value in updates.items():
                redis_client.json().set(self.key(), f".{key}", value)
        return super().save()

    @classmethod
    def get(cls, user_id: str):
        return cls.find(cls.user_id == user_id).first()

    def __repr__(self):
        return f"UserTest(user_id='{self.user_id}', name='{self.name}', age={self.age})"
