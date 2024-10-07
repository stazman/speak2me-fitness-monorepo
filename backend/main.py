from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import test_mongo_connection, init_db, close_mongo_connection

async def lifespan(app: FastAPI):
    
    if not await test_mongo_connection():
        raise RuntimeError("Could not connect to MongoDB")
    await init_db()
    yield

    await close_mongo_connection()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/test")
async def read_root():
    return {"message": "Hello, this is a test endpoint"}