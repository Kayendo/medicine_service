from pydantic import BaseModel, ConfigDict


class Medicine(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    amount: int