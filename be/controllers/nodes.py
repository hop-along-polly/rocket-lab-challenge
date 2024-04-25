from typing import Any, Annotated, Dict, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from be.db.nodes_repository import NodesRepository

router = APIRouter()


record = {
  "Rocket": {
    "Height": 18.000,
    "Mass": 12000.000,
    "Stage1": {
      "Engine1": {
        "Thrust": 9.493,
        "ISP": 12.156
      },
      "Engine2": {
        "Thrust": 9.413,
        "ISP": 11.632
      },
      "Engine3": {
        "Thrust": 9.899,
        "ISP": 12.551
      }
    },
    "Stage2": {
      "Engine1": {
        "Thrust": 1.622,
        "ISP": 15.110
      }
    }
  }
}

def get_nodes_repo():
  return NodesRepository.create()


@router.get('/{root_node}/{sub_node_path:path}')
async def get_sub_nodes(root_node: str, sub_node_path: str, nodes_repo: Annotated[dict, Depends(get_nodes_repo)]) -> JSONResponse:
  node = await nodes_repo.get_node_by_root(root_node)
  curr = node[root_node]
  last_node = root_node
  for n in sub_node_path.split('/'):
    if n not in curr.keys():
      return JSONResponse({ 'message': f'Subnode {n} not found.'}, 404)
    curr = curr[n]
    last_node = n

  return JSONResponse( { last_node: curr }, 200)


@router.get('/{root_node}')
async def get_root_node(root_node: str, nodes_repo: Annotated[dict, Depends(get_nodes_repo)]) -> JSONResponse:
  print('Controller Nodes Repo:', nodes_repo)
  print('Type', type(nodes_repo))
  node = await nodes_repo.get_node_by_root(root_node)
  print('Node', node)
  if not node:
    return JSONResponse({ 'message': f'Unable to find a node with root "{root_node}"'}, 404)

  return JSONResponse(node, 200)


@router.post('/{root_node}/{sub_node_path:path}')
async def create_sub_node(
  root_node: str,
  sub_node_path: str,
  nodes_repo: Annotated[dict, Depends(get_nodes_repo)],
  body: Dict[str,Any]=None
) -> JSONResponse:
  node = await nodes_repo.get_node_by_root(root_node)
  if not node:
    return JSONResponse({ 'message': f'Unable to find a node with root "{root_node}"'}, 404)
  
  return JSONResponse({ 'root': root_node, 'sub_nodes': sub_node_path, 'body': body }, 201)
