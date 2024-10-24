from grpc import aio
from protobuffs.todo import todo_pb2_grpc
from fastapi import Response
from config import TODO_GRPC_SERVER_ADDR

async def grpc_todo_client():
    addr: str = TODO_GRPC_SERVER_ADDR 
    channel = aio.insecure_channel(addr)
    client = todo_pb2_grpc.TodoServiceStub(channel)
    return client