from beanie import Document
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Macronutrients(BaseModel):
    carbohydrates: float  # in grams
    protein: float        # in grams
    fats: float           # in grams
    sugar: float          # in grams

class FoodItem(Document):
    id: str
    food: str
    calories: int
    serving_size: str
    macronutrients: Macronutrients
    created_at: datetime = datetime.utcnow()
    modified_at: Optional[datetime] = None
    user_id: str