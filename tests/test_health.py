from fastapi.testclient import TestClient
import pytest

from be.app import app
from be.controllers.health import get_db_client


class MockDbClient():
  def __init__(self, health_result):
    self.result = health_result

  async def health(self):
    return self.result


@pytest.fixture
def healthy_db_client(mock_db):
  
  def create_mock():
    return MockDbClient('healthy')
  return create_mock

@pytest.fixture
def unhealthy_db_client(mock_db):
  
  def create_mock():
    return MockDbClient('unhealthy')
  return create_mock


def test_health_endpoint_200(healthy_db_client):
  # Arrange
  subject = TestClient(app)
  app.dependency_overrides[get_db_client] = healthy_db_client

  # Act
  actual = subject.get('/v1/health')

  # Assert
  assert 200 == actual.status_code
  assert { 'api': 'healthy', 'db': 'healthy' } == actual.json()


def test_health_endpoint_no_db(unhealthy_db_client):
  # Arrange
  subject = TestClient(app)
  app.dependency_overrides[get_db_client] = unhealthy_db_client

  # Act
  actual = subject.get('/v1/health')

  # Assert
  assert 200 == actual.status_code
  assert { 'api': 'healthy', 'db': 'unhealthy' } == actual.json()
