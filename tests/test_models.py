import pytest

from be.db.models import Node


def test_create_model_from_path():
  # Arrange

  # Act
  actual = Node.create('/Root')

  # Assert
  assert Node('Root', [], {}) == actual


def test_create_model_sub_node():
  # Arrange

  # Act
  actual = Node.create('/Root/Sub')

  # Assert
  assert Node('Root', [Node('Sub')], {}) == actual
