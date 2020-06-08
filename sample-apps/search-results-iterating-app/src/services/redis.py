from redis import Redis
import os


redis = Redis.from_url(os.getenv("REDIS_URL"))
