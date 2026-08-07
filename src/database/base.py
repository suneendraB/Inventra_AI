#this file creates the base class 
# every sql alchemy model in the project inherit from this
# without base , sqlalchemy cannot recognize your models

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Base class for all db models
    Every sqlalchemy models in the project will inherit from this class
    """
    pass