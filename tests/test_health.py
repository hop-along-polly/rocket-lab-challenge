from fastapi.testclient import TestClient
from be.app import app

import pytest


def test_health_endpoint_200():
  # Arrange
  subject = TestClient(app)

  # Act
  actual = subject.get('/v1/health')

  # Assert
  assert 200 == actual.status_code
  assert { 'api': 'healthy', 'db': 'healthy' } == actual.json()


def test_health_endpoint_no_db(mocker):
  # Arrange
  subject = TestClient(app)
  mocker.patch('be.db.client.DbClient.health', return_value='unhealthy')

  # Act
  actual = subject.get('/v1/health')

  # Assert
  assert 200 == actual.status_code
  assert { 'api': 'healthy', 'db': 'unhealthy' } == actual.json()
