from lib.state.state import list_state
from segment.sample.dag import sample

# sample.Source1.run()
# sample.Source2.run()

from repositories.redis.models.test import UserTest
from repositories.redis.connection import redis_client

def test_redis_om():
    user = UserTest(user_id="testuser", name="Test User", age=30)
    user.save()

    retrieved_user = UserTest.get("testuser")

    assert retrieved_user.user_id == user.user_id
    assert retrieved_user.name == user.name
    assert retrieved_user.age == user.age
    print("Redis-OM test passed!")

    # Test partial update
    retrieved_user.save(updates={"name": "Updated User", "age": 31})
    updated_user = UserTest.get("testuser")
    assert updated_user.name == "Updated User"
    assert updated_user.age == 31
    print("Redis-OM partial update test passed!")

test_redis_om()
