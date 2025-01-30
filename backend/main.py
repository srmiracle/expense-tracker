from fastapi import FastAPI
from database import engine
from models import Base
from routes import router

# Create tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Expense Tracker!"}

