from fastapi import FastAPI

from src.core.config import settings

from src.database.connection import check_database_connection

from src.modules.companies.router import router as company_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(company_router)


@app.get("/")
async def root():
    return {
        "message" :  "Welcome to Inventra AI"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": settings.app_name,
        "version" : settings.app_version,    
    }




@app.get("/health/db")
async def database_health():
    """
    Check the db connectivity 
    """
    is_connected, error = await check_database_connection()
    
    if is_connected:
        return {
            "status" : "Healthy",
            "database" : "connected"
        }
    return {
        "status": "unhealthy",
        "database": "disconnected",
        "error" : error       
    }