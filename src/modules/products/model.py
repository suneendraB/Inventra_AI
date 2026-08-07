from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, Text, String

from src.database.base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "Products"
    
    id = Column(Integer, primary_key=True, index=True)
    
    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
    )
    
    product_name = Column(String(255), nullable = False,)
    
    sku = Column(String(100),unique = True, nullable=False)
    
    description = Column(Text)
    category = Column(String(100))
    
    brand = Column(String(100))

    price = Column(
        Numeric(10, 2),
        nullable=False,
    )

    cost_price = Column(
        Numeric(10, 2),
        nullable=False,
    )

    quantity = Column(
        Integer,
        default=0,
    )

    image_url = Column(String(500))

    status = Column(
        String(20),
        default="ACTIVE",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    company = relationship(
        "Company",
        back_populates="products",
    )  