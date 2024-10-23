from typing import Any
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

from clients import grpc_todo_client
from protobuffs import todo_pb2
from google.protobuf.json_format import MessageToDict

router = APIRouter(
    prefix="",
    tags=["grpc hear"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_todo(name: str,
                   completed: bool,
                   day: int,
                   client: Any = Depends(grpc_todo_client)
                   ) -> JSONResponse:
    todo = await client.CreateTodo(
        todo_pb2.CreateTodoRequest(
            name=name,
            completed=completed,
            day=day
        ),
        timeout=5
    )
    return JSONResponse(MessageToDict(todo))