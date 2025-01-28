from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import test_mongo_connection, init_db, close_mongo_connection
from backend.routes import create_router

router = create_router()
async def lifespan(app: FastAPI):
    if not await test_mongo_connection():
        raise RuntimeError("Could not connect to MongoDB")
    await init_db()
    yield
    await close_mongo_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Speak2Me Calorie Tracker API"}
