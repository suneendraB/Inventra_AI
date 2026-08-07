# connection.py = check connections 
# session.py - create the connections 

from sqlalchemy import text

from sqlalchemy.exc import SQLAlchemyError
from src.database.session import engine

async def check_database_connection():
    """
    Check whether the application can connect to the postgreSQL
    
    """
    try:
        async with engine.begin() as connection:
            await connection.execute(text("SELECT 1"))
        
        return True, None
    except SQLAlchemyError as error:
        return False, str(error)
    
    