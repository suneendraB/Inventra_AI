# this file create the connection between the FastAPI and PostgreSQL 

# every request that needs the db will ask for a session

from sqlalchemy.ext.asyncio import(
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from src.core.config import settings

#create the db engine
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    future = True,
)
# engine =  road to postgres 


#create a session factory
# create a new db session when ever fastapi ask for one 
#each request gets its own session 
SessionLocal = async_sessionmaker(
    bind = engine,
    class_= AsyncSession,
    expire_on_commit= False,
)

# Dependency to get db session
# fast api will automatically create db session , pass it to endpoint, close after the request finishes
async def get_db():
    async with SessionLocal() as session:
        yield session


