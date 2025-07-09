from pydantic import BaseModel , field_validator , ConfigDict
from typing import Optional

class TenantInfoModel(BaseModel):
    ApiUrl: str
    AppName: str
    Auth0ClientId: str
    Auth0Domain: str
    Auth0Organization: Optional[str] = None
    BundleId: str
    OktaClientId: Optional[str] = None
    OktaDomain: Optional[str] = None
    PackageName: str
    SentryDsn: str
    TenancyName: str
    TenantId: int

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda s: s[0].lower() + s[1:]  # PascalCase → camelCase
    )
    
    @field_validator("Auth0Domain")
    @classmethod
    def validate_auth0_domain(cls, value):
        if ".auth0" not in value or ".com" not in value:
            raise ValueError("Please provide valid Auth0 Domain")
        return value
    
    @field_validator("BundleId", "PackageName")
    @classmethod
    def validate_com_prefix_fields(cls, value: str, info) -> str:
        if not value.startswith("com."):
            raise ValueError(f"Please provide valid {info.field_name}")
        return value
