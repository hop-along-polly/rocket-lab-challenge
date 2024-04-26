from typing import Any, Dict, List

from motor.motor_asyncio import AsyncIOMotorClient

from be.config import get_config

class DbClient:

  def __init__(self, client):
    self._client = client

  @classmethod
  def create(cls):
    cfg = get_config()
    return cls(AsyncIOMotorClient(cfg.mongodb_uri))

  def get_collection(self, collection_name: str):
    return self._client['rocket-lab'][collection_name]

  async def health(self):
    try:
      await self._client.admin.command('ping')
    except Exception as e:
      print('Mongo Connection Error:', e)  # TODO consider implementing logging before final submission
      return 'unhealthy'
    finally:
      return 'healthy'
