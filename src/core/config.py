# ONE RESPONSIBILITY - READ ENV VARIABLES AND EXPOSE THEM TO APPLICATION

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug : bool
    
    database_url : str
    
    secret_key: str
    algorithm: str
    access_token_expire_minutes : int
    
    
    class Config:
        env_file = ".env"

settings = Settings()

    
