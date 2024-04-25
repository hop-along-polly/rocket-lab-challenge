import mongomock
import pytest


@pytest.fixture
def mock_db(mocker):
  in_memory_db = mongomock.MongoClient()

  return in_memory_db
