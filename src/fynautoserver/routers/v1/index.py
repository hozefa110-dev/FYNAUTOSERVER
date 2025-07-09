from fastapi import APIRouter
from fynautoserver.routers.v1.tenant_info.tenant_info import router

router_v1 = APIRouter()

router_v1.include_router(router,prefix='/tenantInfo')