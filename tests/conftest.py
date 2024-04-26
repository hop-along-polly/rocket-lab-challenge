from mongomock_motor import AsyncMongoMockClient
import pytest


@pytest.fixture
def mock_db():
  in_memory_db = AsyncMongoMockClient()

  return in_memory_db
