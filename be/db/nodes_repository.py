from typing import Dict, List

from motor.motor_asyncio import AsyncIOMotorClient

from be.config import get_config


class NodesRepository:
  # I should be able to pass the in-memory client here for testing
  def __init__(self, client):
    self._collection = client['rocket-lab']['nodes']

  @classmethod
  def create(cls):
    cfg = get_config()
    mongo_client = AsyncIOMotorClient(cfg.mongodb_uri)
    return cls(mongo_client)

  async def get_node(self, root: str, path: List[str]) -> Dict | None:
    query_path = f"{root}.{'.'.join(path)}".strip('.')
    query = { query_path: { "$exists": True } }
    projection = { query_path: True, '_id': False}

    try:
      return await self._collection.find_one(query, projection)
    except Exception as e:
      print(e) # TODO Logging?
      return None

  async def add_node_at_path(self, root: str, new_node_path: List[str], body=None):
    existing = await self.get_node(root, [])
    if not existing:
      return None

    query_path = [root]
    insert_path = [root]

    curr = existing[root]
    for p in new_node_path:
      if p in curr.keys():
        query_path.append(p)
        insert_path.append(p)
      else:
        insert_path.append(p)
      curr = curr.get(p, {})

    query = { '.'.join(query_path): { "$exists": True } }
    update = {
      '$set': {
        '.'.join(insert_path): {} if not body else body
      }
    }

    return await self._collection.find_one_and_update(query, update, { "_id": False }, return_document=True)
