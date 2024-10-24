import typing
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse


from router import router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

app = FastAPI()


app.include_router(router)