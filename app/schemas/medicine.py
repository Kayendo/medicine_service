from sqlalchemy import Column, String, DateTime, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base



class DBMedicine(Base): 
	__tablename__ = 'medicines'

	name = Column(String, primary_key=True) 
	amount = Column(Integer) 
