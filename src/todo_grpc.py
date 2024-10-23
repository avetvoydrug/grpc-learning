import logging
from services.todo import service_runner
import asyncio
from config import TODO_GRPC_SERVER_ADDR


if __name__ == "__main__":
    asyncio.run(service_runner(TODO_GRPC_SERVER_ADDR))