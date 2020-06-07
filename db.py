import redis
# Use Redis as a Database
# Redis Documentation >  https://pypi.org/project/redis/
r = redis.StrictRedis(decode_responses=True)
