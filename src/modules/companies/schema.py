from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class CompanyCreate(BaseModel):
    company_name: str
    email: EmailStr
    phone: str | None=None
    address: str | None=None
    
class CompanyUpdate(BaseModel):
    company_name: str | None = None
    email: EmailStr | None = None
    phone: str | None= None
    address : str | None = None
    is_active: bool | None = None

class CompanyResponse(BaseModel):
    id: int
    company_name: str
    email: EmailStr
    phone: str | None
    address: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    # this is the pydantic v2 way
    # API response model 
    # convert sqlalchemy object into JSON
    
    # looks at object attributes
    
    
    