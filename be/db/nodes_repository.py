from typing import Dict

from motor.motor_asyncio import AsyncIOMotorClient

from be.config import get_config


class NodesRepository:
  # I can pass the in-memory client here for testing
  def __init__(self, client):
    self._collection = client['rocket-lab']['nodes']

  @classmethod
  def create(cls):
    cfg = get_config()
    mongo_client = AsyncIOMotorClient(cfg.mongodb_uri)
    return cls(mongo_client)

  async def get_node_by_root(self, root_node: str) -> Dict | None:
    query = { root_node: { "$exists": True } }
    try:
      return await self._collection.find_one(query, { '_id': False })
    except Exception as e:
      print(e)
      return None
