from uuid import UUID
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Body

from app.services.medicine_service import MedicineService
from app.models.medicine import Medicine

medicine_router = APIRouter(prefix="/medicines", tags=["Medicines"])

@medicine_router.get("/", response_model=list[Medicine])
def get_all_medicines(medicine_service: MedicineService = Depends(MedicineService)) -> list[Medicine]:

    return medicine_service.get_all_medicines()

@medicine_router.post("/", response_model=Medicine)
def create_medicine(medicine: Medicine, medicine_service: MedicineService = Depends(MedicineService)) -> Medicine:
    try:
        new_medicine = medicine_service.create_medicine(medicine)
        return new_medicine
    except Exception as e:  
        raise HTTPException(status_code=500, detail=f"Error creating medicine: {str(e)}")