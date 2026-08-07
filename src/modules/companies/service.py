from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.companies.repository import CompanyRepository

from src.modules.companies.schema import CompanyCreate,CompanyUpdate

from src.core.exceptions import (CompanyAlreadyExistsException,
                                 CompanyNotFoundException,)

company_repository = CompanyRepository()


class CompanyService:
    async def create_company(
        self, 
        db: AsyncSession,
        company_data: CompanyCreate
    ):
        
        existing_company = await company_repository.get_company_by_email(
            db,
            company_data.email
        )
        
        if existing_company:
            raise CompanyAlreadyExistsException()
            
        return await company_repository.create_company(
            db,
            company_data,
        )
        
    async def get_all_companies(
        self, 
        db: AsyncSession,
        page: int,
        limit: int,
        search: str | None = None,
    ):
        return await company_repository.get_all_companies(
            db,
            page,
            limit,
            search,
            )
    
    async def get_company_by_id(self,
                            db:AsyncSession,
                            company_id: int,):
        company = await company_repository.get_company_by_id(
            db,
            company_id,
        )
        
        if company is None:
            raise CompanyNotFoundException()
        return company

    async def update_company(
        self,
        db: AsyncSession,
        company_id: int,
        company_data: CompanyUpdate,
    ):
        company = await company_repository.get_company_by_id(
            db,
            company_id
        )
        
        if company is None:
            raise CompanyNotFoundException()
        return await company_repository.update_company(
            db,
            company,
            company_data,
        )
        
    async def delete_company(
        self,
        db: AsyncSession,
        company_id: int,
    ):
        company = await company_repository.get_company_by_id(
            db,
            company_id,
        )
        
        if company is None:
            raise CompanyNotFoundException()
        
        await company_repository.delete_company(
            db,
            company,
            )
        return {
            "message": "Company deleted successfully"
        }
    