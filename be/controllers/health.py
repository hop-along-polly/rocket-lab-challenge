from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from be.db.client import DbClient

router = APIRouter()


@router.get('/health')
async def health(db = Depends(DbClient.create)):
  db_status = await db.health()
  return JSONResponse({ 'api': 'healthy', 'db': db_status }, 200)
