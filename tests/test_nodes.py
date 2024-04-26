import pytest
from fastapi.testclient import TestClient

from be.app import app
from be.controllers.nodes import get_nodes_repo
from be.db.nodes_repository import NodesRepository


@pytest.fixture
def mock_nodes_repo(mock_db):
  def create_mock():
    return NodesRepository(mock_db)

  return create_mock


def test_get_root_node_not_found(mock_db):
  # Arrange
  subject = TestClient(app)

  # Act
  actual = subject.get('/v1/dne')

  # Assert
  assert 404 == actual.status_code
  assert { 'message': 'Unable to find a node with root "dne"'} == actual.json()


# def test_get_root_node_no_sub_nodes(mock_db, mock_nodes_repo):
#   # Arrange
#   mock_db['rocket-lab']['nodes'].insert_one({ "Root": {} })
#   subject = TestClient(app)

#   app.dependency_overrides[get_nodes_repo] = mock_nodes_repo

#   # Act
#   actual = subject.get('/v1/Root')

#   # Assert
#   # assert { 'message': 'Unable to find a node with root "dne"'} == actual.json()
#   assert 200 == actual.status_code
