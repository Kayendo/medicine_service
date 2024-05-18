# from sqlalchemy.orm import Session 

# from app.database import get_db 
# from app.models.medicine import Medicine 
# from app.schemas.medicine import Medicine as DBMedicine

# class MedicineRepo():
# 	def __init__(self) -> None:
# 		self.db = next(get_db())

# 	def create_medicine(self, medicine: DBMedicine) -> Medicine:
# 		new_medicine = Medicine(name=medicine.name, amount=medicine.amount)
# 		self.db.add(new_medicine)
# 		self.db.commit()
# 		return new_medicine

# 	def get_all_medicines(self) -> list[Medicine]:
# 		return self.db.query(Medicine).all()

# 	def get_medicine_by_name(self, name: str) -> Medicine:
# 		return self.db.query(Medicine).filter(Medicine.name == name).first()
