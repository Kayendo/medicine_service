import asyncio
from fastapi import FastAPI
from app import rabbitmq
from app.settings import settings
from app.endpoints.router import medicine_router

from app.schemas.base_schema import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

# (Assuming database.py and models.py are in place)

engine = create_engine(settings.postgres_url, echo=True)  # Get engine from database.py

# Create all tables based on models (assuming your application has multiple models)
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Medicine Service') 

@app.on_event('startup') 
def startup(): 
	loop = asyncio.get_event_loop() 
	asyncio.ensure_future(rabbitmq.consume(loop)) 

app.include_router(medicine_router, prefix='/api') 