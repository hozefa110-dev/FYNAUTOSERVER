from beanie import Document
from typing import Optional

class TenantInfoSchema(Document):
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

    class Setting():
        name = 'tenant_info'