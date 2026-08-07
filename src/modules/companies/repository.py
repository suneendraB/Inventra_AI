# only one resp= talk to database

# only db operations 


from sqlalchemy import select , or_, asc, desc

from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.companies.model import Company
from src.modules.companies.schema import CompanyCreate, CompanyUpdate
from src.modules.companies.query import CompanyQueryParams


class CompanyRepository:
    async def create_company(
        self,
        db: AsyncSession, 
        company_data: CompanyCreate,) -> Company:
        
        # creates a python object 
        company = Company(
            company_name = company_data.company_name,
            email = company_data.email,
            phone= company_data.phone,
            address = company_data.address,
        )  
        #mark this object to be inserted 
        db.add(company)
        # executes the sql 
        await db.commit()
        # reloads the object from the db
        await db.refresh(company)
        #return the sqlalchemy object
        return company
    
        
    async def get_company_by_email(
        self,
        db: AsyncSession,
        email: str,) -> Company | None:
        
        # execute() runs the sql query
        result = await db.execute(
            select(Company).where(Company.email == email)
        )
        # return one Company object if found , otherwise None
        return result.scalar_one_or_none() 
    
    async def get_all_companies(
        self, 
        db: AsyncSession,
        page: int,
        limit: int,
        query_params: CompanyQueryParams,
    ) -> list[Company]:
        
        query = select(Company)
        
        # search 
        if query_params.search:
            query = query.where(
                or_(
                    Company.company_name.ilike(f"%{query_params.search}%"),
                    Company.email.ilike(f"%{query_params.search}%"),
                )
            )
        # Filter
        if query_params.is_active is not None:
            query= query.where(
                Company.is_active == query_params.is_active
            )
        
        #Allowed sorting columns
        allowed_sort_fields = {
            "id" : Company.id,
            "company_name": Company.company_name,
            "email": Company.email,
            "created_at" : Company.created_at,
        }
        
        
        # Sorting
        sort_column = allowed_sort_fields.get(
            query_params.sort_by,
            Company.id,
        )
        
        if query_params.sort_order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))
            
        #Pagination
        offset = (page - 1) * limit
        
        query = query.offset(offset).limit(limit)
        
        result = await db.execute(query)
        
        return result.scalars().all()
    # scalars.all mean - give all companies list
    
    async def get_company_by_id(
        self,
        db: AsyncSession,
        company_id: int,
    ) -> Company | None:

        result = await db.execute(
            select(Company).where(
                Company.id == company_id
            )
        )

        return result.scalar_one_or_none()
    
    async def update_company(
        self, 
        db: AsyncSession, 
        company: Company,
        company_data: CompanyUpdate,)-> Company:
        
        update_data = company_data.model_dump(exclude_unset= True)
        for key, value in self.update_data.items():
            setattr(company, key, value)
            
        await db.commit()
        
        await db.refresh(company)
        
        return company
    
    async def delete_company(
        self,
        db: AsyncSession,
        company: Company,
    ) -> None:
        await db.delete(company)
        await db.commit()
        
        
        