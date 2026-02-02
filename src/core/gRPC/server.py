import grpc
from proto import catalog_pb2_grpc

from src.core.gRPC.catalog_server import CatalogServicer


async def serve():
    server = grpc.aio.server()
    catalog_pb2_grpc.add_CatologServicer_to_server(CatalogServicer, server)
    server.add_insecure_port("[::]:50051...")
    print("gRPC сервер запущен на порту 50051...")
    await server.start()
    await server.wait_for_termination()