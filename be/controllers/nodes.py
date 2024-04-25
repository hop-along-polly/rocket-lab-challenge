from typing import Any, Dict

from fastapi import APIRouter
from fastapi.responses import JSONResponse


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


@router.get('/{root_node}/{sub_node_path:path}')
def get_sub_nodes(root_node: str, sub_node_path: str) -> JSONResponse:
  return JSONResponse({ 'root': root_node, 'Sub Node Path': sub_node_path}, 200)


@router.get('/{root_node}')
def get_root_node(root_node: str) -> JSONResponse:
  return JSONResponse({ 'root': root_node }, 200)


@router.post('/{root_node}/{sub_node_path:path}')
def create_sub_node(root_node: str, sub_node_path: str, body: Dict[str,Any]=None) -> JSONResponse:
  return JSONResponse({
    'root': root_node,
    'sub node path': sub_node_path,
    'body': body
  }, 201)
