from fastapi import APIRouter, FastAPI
from fynautoserver.models.index import TenantInfoModel
from fynautoserver.controller.tenant_info_crud import create_tenant_info , getTenantInfoByTenancyName
from fynautoserver.utils.index import create_response
from fynautoserver.models.index import ResponseModel


app = FastAPI()

router = APIRouter()

@router.get('/getTenantInfo',response_model=ResponseModel)
async def getTenantInfo():
    return create_response(success=True,result={"msg":'hi there'})

@router.get('/getTenantIdByName')
async def getTenantIdByName(tenancyName: str):
    response = await getTenantInfoByTenancyName(tenancyName)
    return response
    
@router.post('/setTenantInfo',response_model=ResponseModel)
async def setTenantInfo(payload:TenantInfoModel):
    try:
        tenant = await create_tenant_info(payload)
        return create_response(success=True, result=tenant, status_code=201)
    except Exception as e:
        print(f"error during creating tenant file : {e}")
        return create_response(
            success=False,
            error_message="Failed to create tenant. Please try again.",
            error_detail=str(e),
            status_code=500,
        )
        