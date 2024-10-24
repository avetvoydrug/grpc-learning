from services.server import services_runner 
import asyncio
from config import TODO_GRPC_SERVER_ADDR


if __name__ == "__main__":
    addr: str = TODO_GRPC_SERVER_ADDR
    asyncio.run(services_runner(addr))