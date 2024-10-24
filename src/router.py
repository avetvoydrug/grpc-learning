from typing import Any
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from grpc.aio import AioRpcError

from clients import grpc_todo_client
from protobuffs.todo import todo_pb2
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
    print(f"from route {client}")
    try:
        print("from route, try")
        todo = await client.CreateTodo(
            todo_pb2.CreateTodoRequest(
                name=name,
                completed=completed,
                day=day
            ),
            timeout=5
        )
    except AioRpcError as e:
        print(f"Ошибка: {e}")
        raise HTTPException(status_code=404, detail=e.details())
    return JSONResponse(MessageToDict(todo))

@router.get("/get-todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(todo_id: int, client: Any = Depends(grpc_todo_client)):
    try:
        todo = await client.ReadTodo(
            todo_pb2.ReadTodoRequest(
                id=todo_id
            ),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(todo))

@router.get("/get-todos-list", status_code=status.HTTP_200_OK)
async def get_todos_list(client: Any = Depends(grpc_todo_client)):
    try:
        todos = await client.ListTodos(
            todo_pb2.ListTodosRequest(),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(todos))


@router.patch("/update-todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int,
                      name: str,
                      completed: bool,
                      client: Any = Depends(grpc_todo_client)):
    try:
        todo = await client.UpdateTodo(
            todo_pb2.UpdateTodoRequest(
                id=todo_id,
                name=name,
                completed=completed
            ),
            timeout=5
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return JSONResponse(MessageToDict(todo))

@router.delete("/delete-todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int,
                      client: Any = Depends(grpc_todo_client)):
    try:
        todo = await client.DeleteTodo(
            todo_pb2.DeleteTodoRequest(
                id=todo_id
            ),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(todo))