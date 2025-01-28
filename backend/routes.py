from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime
from .models import FoodItem, Macronutrients

def create_router() -> APIRouter:
    router = APIRouter()

    @router.post("/food_items/add")
    async def add_food_item(
        food: str, calories: int, serving_size: str, 
        carbohydrates: float, protein: float, fats: float, sugar: float,
        user_id: str
    ):
        macronutrients = Macronutrients(
            carbohydrates=carbohydrates,
            protein=protein,
            fats=fats,
            sugar=sugar
        )
        item = FoodItem(
            id=str(uuid4()),
            food=food,
            calories=calories,
            serving_size=serving_size,
            macronutrients=macronutrients,
            created_at=datetime.utcnow(),
            user_id=user_id
        )
        await item.insert()
        return {"message": "Food item added successfully", "item": item}

    @router.get("/food_items")
    async def get_all_food_items():
        items = await FoodItem.find_all().to_list()
        return {"items": items}

    @router.get("/food_items/total")
    async def get_total_calories(user_id: str):
        items = await FoodItem.find(FoodItem.user_id == user_id).to_list()
        total = sum(item.calories for item in items)
        return {"total_calories": total}

    @router.put("/food_items/{item_id}")
    async def update_food_item(
        item_id: str, food: str, calories: int, serving_size: str,
        carbohydrates: float, protein: float, fats: float, sugar: float
    ):
        item = await FoodItem.get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        item.food = food
        item.calories = calories
        item.serving_size = serving_size
        item.macronutrients = Macronutrients(
            carbohydrates=carbohydrates,
            protein=protein,
            fats=fats,
            sugar=sugar
        )
        item.modified_at = datetime.utcnow()
        await item.save()
        return {"message": "Food item updated successfully", "item": item}

    @router.delete("/food_items/{item_id}")
    async def delete_food_item(item_id: str):
        item = await FoodItem.get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        await item.delete()
        return {"message": "Food item deleted successfully"}

    return router