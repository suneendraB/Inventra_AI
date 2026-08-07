from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func
from src.database.base import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key = True, index=True)
    
    company_name = Column(String(100), unique=True, nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    phone = Column(String(20), nullable=True)

    address = Column(Text, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    
    products = relationship("Product",back_populates="company",) 