from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession


from src.database.session import get_db
from src.modules.companies.schema import(
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate
)

from src.modules.companies.service import CompanyService



router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

company_service = CompanyService()


@router.post(
    "",
    response_model=CompanyResponse,
    status_code=201,
    )
async def create_company(
    company_data: CompanyCreate,
    db: AsyncSession= Depends(get_db),
):
    return await company_service.create_company(
        db,
        company_data,
    )
    
# db: AsyncSession = Depends(get_db)
# fastapi before calling this end point - create a db session and pass it to me 




@router.get(
    "",
    response_model=list[CompanyResponse],
)
async def get_all_companies(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    search: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
):
    return await company_service.get_all_companies(
        db,
        page,
        limit,
        search,
        )



@router.get(
    "/{company_id}",
    response_model= CompanyResponse,
)
async def get_company_by_id(
    company_id: int,
    db: AsyncSession= Depends(get_db),
):
    return await company_service.get_company_by_id(
        db,
        company_id,
        )
    
@router.put("/{company_id}",
            response_model=CompanyResponse,
            )
async def update_company(
    company_id: int,
    company_data: CompanyUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await company_service.update_company(
        db,
        company_id,
        company_data,
    )


@router.delete(
    "/{company_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_company(
    company_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await company_service.delete_company(
        db,
        company_id,
    )