from grpc import aio

from protobuffs import todo_pb2
from protobuffs import todo_pb2_grpc

from sqlalchemy import insert

from models.models import Todo
from database import async_session_maker

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    async def CreateTodo(self, request, context):
        async with async_session_maker() as session:
            stmt = (insert(Todo)
                    .values(name=request.name,
                            completed=request.completed,
                            day=request.day))
            result = await session.execute(stmt)
            await session.commit()
            res = result.scalar_one()
            print(f"res= {res}")
            # return res
            return todo_pb2.CreateTodoResponse(todo=res[0])
        
async def service_runner(addr):
    server = aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoService(), server
    )
    server.add_insecure_port(addr)
    print(f"Todo service ran at: {addr}")
    await server.start()
    await server.wait_for_termination()
