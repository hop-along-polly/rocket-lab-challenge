from typing import Any, Annotated, Dict, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from be.db.nodes_repository import NodesRepository

router = APIRouter()

def get_nodes_repo():
  return NodesRepository.create()


@router.get('/{root_node}/{sub_node_path:path}')
async def get_sub_nodes(root_node: str, sub_node_path: str, nodes_repo: Annotated[dict, Depends(get_nodes_repo)]) -> JSONResponse:
  node = await nodes_repo.get_node(root_node, sub_node_path.split('/'))
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
  node = await nodes_repo.get_node(root_node, [])
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
  existing = await nodes_repo.get_node(root_node, [])
  if not existing:
    return JSONResponse({ 'message': f'Unable to find a node with root "{root_node}"'}, 404)

  result = await nodes_repo.add_node_at_path(root_node, sub_node_path.strip('/').split('/'), body)
  if not result:
    return JSONResponse({ 'message': f'Unable to update {root_node}'}, 500)

  return JSONResponse(result, 200)
