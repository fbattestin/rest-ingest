"""
Dependency for Redis connection.
"""
import redis.asyncio as aioredis
from common.config.settings import settings
from common.utils.logging import setup_logging

logger = setup_logging()

async def get_redis():
    """
    Initializes and returns the Redis connection.
    """
    logger.info("Initializing Redis connection")
    return aioredis.from_url(settings.REDIS_URL)