from typing import Any, Dict, List

# TODO Not sure I'm going to want this repository still

class Node:

  def __init__(self, name, children=None, properties=None):
    self.name = name
    self.children = children if children else []
    self.properties = properties if properties else {}

  @classmethod
  def create(cls, raw_node: str | Dict[Any, Any]):
    if isinstance(raw_node, str):
      nodes = raw_node.strip('/').split('/')
      return cls(
        nodes[0],
        Node.create('/'.join(nodes[1:])),{})
    else:
      return cls('')
  
  def __eq__(self, other):
    print(f'{self.name}=={other.name}')
    print(f'{self.children}=={other.children}')
    print(f'{self.properties}=={other.properties}')
    return self.name == other.name and \
      self.children == other.children and \
      self.properties == other.properties
