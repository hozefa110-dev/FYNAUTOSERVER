from fastapi import APIRouter
from fynautoserver.routers.v1.index import router_v1

router = APIRouter()

router.include_router(router_v1,prefix='/v1')