import grpc
from proto import catalog_pb2_grpc


class GRPCClient:
    def __init__(self):
        self.channel = None
        self.stub = None


    async def connect(self):
        self.channel = grpc.aio.insecure_channel(f"localhost:{50051}")
        self.stub = catalog_pb2_grpc.CatalogStub(self.channel)
        return self


    async def disconnect(self):
        if self.channel:
            await self.channel.close()


    def get_stub(self):
        return self.stub


grpc_client = GRPCClient()