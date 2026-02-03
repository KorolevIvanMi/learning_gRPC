import grpc
import asyncio
from proto import catalog_pb2_grpc

from src.core.gRPC.catalog_server import CatalogServicer


class GRPCServer:
    def __init__(self, port: int = 50051):
        self.port = port
        self.server = None


    async def start(self):
        self.server = grpc.aio.server()
        catalog_pb2_grpc.add_CatalogServicer_to_server(CatalogServicer(), self.server)
        self.server.add_insecure_port(f"[::]:{self.port}")
        await self.server.start()
        print(f"gRPC сервер запущен на порту {self.port}")
        return self
    
    async def serve_forever(self):
        try:
            if not self.server:
                await self.start()
            print(f"🔄 gRPC сервер слушает на порту {self.port}")
            await self.server.wait_for_termination()
        except Exception as e:
            print(f"Ошибка в gRPC сервере: {e}")
            raise

    async def stop(self):
        if self.server:
            await self.server.stop(0)
            print("gRPC сервер остановлен")