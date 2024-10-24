from protobuffs.todo import todo_pb2 as todo_pb2
from protobuffs.todo.todo_pb2_grpc import TodoServiceServicer

from sqlalchemy import insert, select, update, delete
from grpc.aio import AioRpcError

from models.models import Todo
from schemas.todo import TodoDTO
from database import async_session_maker

class TodoService(TodoServiceServicer):
    async def CreateTodo(self, request, context):
        print("from service")
        async with async_session_maker() as session:
            stmt = (insert(Todo).returning(Todo)
                    .values(name=request.name,
                            completed=request.completed,
                            day=request.day))
            result = await session.execute(stmt)
            await session.commit()
            res = result.scalar()
            todo = TodoDTO.model_validate(res).model_dump()
            print(f"res= {todo}")
            return todo_pb2.CreateTodoResponse(todo=todo)

        
    async def ReadTodo(self, request, context):
        async with async_session_maker() as session:
            query = (select(Todo)
                        .where(Todo.id==request.id))
            result = await session.execute(query)
            result = result.scalar()
            todo = TodoDTO.model_validate(result).model_dump()
            return todo_pb2.ReadTodoResponse(todo=todo)


        
    async def ListTodos(self, request, context):
        async with async_session_maker() as session:
            query = (select(Todo))
            result = await session.execute(query)
            result = result.scalars().all()
            todos = [TodoDTO.model_validate(row).model_dump() for row in result]
            return todo_pb2.ListTodosResponse(todos=todos)

        
    async def UpdateTodo(self, request, context):
        async with async_session_maker() as session:
            stmt = (update(Todo)
                    .returning(Todo)
                    .where(Todo.id==request.id)
                    .values({"name": request.name, 
                            "completed":request.completed}))
            result = await session.execute(stmt)
            await session.commit()
            result = result.scalar()
            print(result)
            todo = TodoDTO.model_validate(result).model_dump()
            return todo_pb2.UpdateTodoResponse(todo=todo)

    
    async def DeleteTodo(self, request, context):
        async with async_session_maker() as session:
            stmt = (delete(Todo)
                    .where(Todo.id==request.id))
            await session.execute(stmt)
            await session.commit()
            return todo_pb2.DeleteTodoResponse(success=True)
