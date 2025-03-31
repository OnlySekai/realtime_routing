from config import REDIS_HOST, REDIS_PORT, REDIS_DB
import redis

class RedisConnectionRepository:
    """
    Repository for managing Redis connections.
    """

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB):
        self.host = host
        self.port = port
        self.db = db
        self.connection = None

    def connect(self):
        """
        Establishes and returns a connection to the Redis server.
        """
        try:
            self.connection = redis.StrictRedis(
                host=self.host,
                port=self.port,
                db=self.db,
                decode_responses=True  # Ensures responses are returned as strings
            )
            # Test the connection
            self.connection.ping()
            print("Connected to Redis successfully!")
        except redis.ConnectionError as e:
            print(f"Failed to connect to Redis: {e}")
            self.connection = None

    def get_connection(self):
        """
        Returns the Redis connection. Establishes it if not already connected.
        """
        if not self.connection:
            self.connect()
        return self.connection


# Usage
redis_client = RedisConnectionRepository()