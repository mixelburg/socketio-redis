import redis

redis_connection = redis.from_url('')
redis_connection.ping()
