from grpc import aio
from protobuffs import todo_pb2_grpc
from fastapi import Response
from config import TODO_GRPC_SERVER_ADDR

async def grpc_todo_client():
    channel = aio.insecure_channel(TODO_GRPC_SERVER_ADDR)
    client = todo_pb2_grpc.TodoServiceStub(channel)
    return client