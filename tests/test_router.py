from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Body

from app.services.medicine_service import MedicineService
from app.models.medicine import Medicine

time.sleep(5)
base_url = 'http://localhost:8001/api'

@pytest.fixture(scope='session')
def medicine_data() -> tuple[UUID, str, datetime]:
    return (uuid4(), 'address_1', datetime.now())