import pytest
from fastapi.testclient import TestClient

from be.app import app
from be.controllers.nodes import get_nodes_repo
from be.db.nodes_repository import NodesRepository


@pytest.fixture
def mock_nodes_repo(mock_db):
  def create_mock():
    repo = NodesRepository(mock_db)
    return repo

  return create_mock


@pytest.mark.asyncio
@pytest.mark.parametrize('record,path,expected', [
  (None, '/v1/dne', { 'status_code': 404, 'body': {'message': 'Unable to find a node with root "dne"'} }),
  ({ 'Root': {} }, '/v1/Root', { 'status_code': 200, 'body': { 'Root': {} } }),
  ({ 'Root': { 'Sub': {} }}, '/v1/Root', { 'status_code': 200, 'body': { 'Root': { 'Sub': {} } } }),
  ({ 'Root': { 'Sub': { 'Prop1': 3.14 } }}, '/v1/Root', { 'status_code': 200, 'body': { 'Root': { 'Sub': { 'Prop1': 3.14 } } } })
])
async def test_get_root_node(mock_db, mock_nodes_repo, record, path, expected):
  # Arrange
  if record:
    await mock_db['rocket-lab']['nodes'].insert_one(record)

  subject = TestClient(app)
  app.dependency_overrides[get_nodes_repo] = mock_nodes_repo

  # Act
  actual = subject.get(path)

  # Assert
  assert expected['status_code'] == actual.status_code
  assert expected['body'] == actual.json()


@pytest.mark.asyncio
@pytest.mark.parametrize('record,path,body,expected', [
  (None, '/v1/dne/sub-dne', None, { 'status_code': 404, 'body': { 'message': 'Unable to find a node with root "dne"' }}),
  ({'Root': {}}, '/v1/Root/Sub', None, { 'status_code': 200, 'body': { 'Root': { 'Sub': {} } }}),
  ({'Root': {}}, '/v1/Root/Sub', { 'prop1': 3.14 }, { 'status_code': 200, 'body': { 'Root': { 'Sub': { 'prop1': 3.14 } } }})
])
async def test_create_sub_node(mock_db, mock_nodes_repo, record, path, body, expected):
# Arrange
  if record:
    await mock_db['rocket-lab']['nodes'].insert_one(record)

  subject = TestClient(app)
  app.dependency_overrides[get_nodes_repo] = mock_nodes_repo

  # Act
  actual = subject.post(path, json=body)

  # Assert
  assert expected['status_code'] == actual.status_code
  assert expected['body'] == actual.json()
