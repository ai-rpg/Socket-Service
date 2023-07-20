import json
import redis
from domain.game_caches_model import GameCache
from interface.i_redis_repository import IRedisRepository
from config import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, NAME
from logger import log


class RedisRepository(IRedisRepository):
    def __init__(self):
        log.info("Connection to Redis", extra={"tags": {"application": NAME}})
        pool = redis.ConnectionPool(
            host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD
        )
        self.redis = redis.Redis(connection_pool=pool)

    def set(self, game_cache: GameCache):
        try:
            self.redis.set(game_cache.user_id, game_cache.toJSON())
        except Exception as e:
            log.error("redis_set", extra={"tags": {"application": NAME}}, exc_info=True)

    def get(self, user_id):
        return self.redis.get(user_id)
