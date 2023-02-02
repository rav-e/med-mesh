from fastapi import FastAPI
from .database import Database
from .auth import auth_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await Database.establish_db_connection()


@app.on_event("shutdown")
async def shutdown():
    await Database.close_db_connection()


@app.get("/")
async def root():
    return "Med Mesh APIs"


app.include_router(auth_router, tags=["Authentication"], prefix="/auth")
