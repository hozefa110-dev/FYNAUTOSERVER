from fastapi import APIRouter
from fynautoserver.routers.v1.tenant_info.tenant_info import router as tenant_info_router
from fynautoserver.routers.v1.file_configs.file_configs import router as file_configs_router

router_v1 = APIRouter()

router_v1.include_router(tenant_info_router,prefix='/tenantInfo')
router_v1.include_router(file_configs_router,prefix='/fileConfigs')