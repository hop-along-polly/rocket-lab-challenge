from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from be.db.client import DbClient

router = APIRouter()


def get_db_client():
  return DbClient.create()

@router.get('/health')
async def health(db: Annotated[dict, Depends(get_db_client)]):
  db_status = await db.health()
  return JSONResponse({ 'api': 'healthy', 'db': db_status }, 200)
