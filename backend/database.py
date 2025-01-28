import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document
from dotenv import load_dotenv
from typing import Optional
from .models import FoodItem

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(MONGODB_URL)
db = client["s2m"]

class User(Document):
    name: str
    email: str
    age: Optional[int]
async def test_mongo_connection():
    
    try:
        await client.admin.command("ping")
        print("MongoDB connected successfully")
        return True
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False

async def init_db():
    client = AsyncIOMotorClient("your-mongodb-connection-string")
    await init_beanie(database=client["speak2me"], document_models=[FoodItem])
    
async def close_mongo_connection():
    client.close()

