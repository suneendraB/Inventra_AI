from pydantic import BaseModel


class CompanyQueryParams(BaseModel):
    page: int = 1
    limit: int = 10
    search:str | None = None
    sort_by: str = "id"
    sort_order: str = "asc"
    is_active: bool | None = None
    
    