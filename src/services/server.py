import logging
from grpc import aio

from protobuffs.todo import todo_pb2 as todo_pb2
from protobuffs.todo.todo_pb2_grpc import add_TodoServiceServicer_to_server

#services
from .todo_service import TodoService

async def services_runner(addr):
    server = aio.server()
    add_TodoServiceServicer_to_server(
        TodoService(), server
    )
    server.add_insecure_port(addr)
    print(f"server started at: {addr}")
    # logging.basicConfig()
    # logging.info(f"Todo server starter at: {addr}")
    await server.start()
    await server.wait_for_termination()