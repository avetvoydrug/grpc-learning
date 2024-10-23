import typing
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from database import create_db_and_tables

from router import router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

app = FastAPI()

@app.get("/")
async def ping():
    return {"ping": True}

app.include_router(router)