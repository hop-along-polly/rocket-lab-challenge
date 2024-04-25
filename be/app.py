from fastapi import FastAPI, APIRouter

from be.controllers.health import router as health_router
from be.controllers.nodes import router as node_router

app = FastAPI()
router = APIRouter(prefix='/v1') # TODO I may remove this prefix just to match the example API endpoints

router.include_router(health_router) # Add health routes
router.include_router(node_router) # Add health routes
app.include_router(router)
