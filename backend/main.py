from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this if your frontend runs on a different URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

