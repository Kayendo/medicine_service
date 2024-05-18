from uuid import UUID
import random
from datetime import datetime

from app.models.medicine import Medicine
# from app.repositories.db_medicine_repo import MedicineRepo

from app.database import get_db 
from app.models.medicine import Medicine 
from app.schemas.medicine import DBMedicine as DBMedicine


class MedicineService:
    def __init__(self) -> None:
        self.db = next(get_db())

    def create_medicine(self, medicine: DBMedicine) -> DBMedicine:
        new_medicine = DBMedicine(name=medicine.name, amount=medicine.amount)
        self.db.add(new_medicine)
        self.db.commit()
        self.db.refresh(new_medicine)  # Ensure ID is populated
        return new_medicine

    def get_all_medicines(self) -> list[DBMedicine]:
        return self.db.query(DBMedicine).all()

    def get_medicine_by_name(self, name: str) -> Medicine:
        return self.db.query(Medicine).filter(Medicine.name == name).first()
