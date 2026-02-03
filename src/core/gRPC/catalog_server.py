from proto import catalog_pb2_grpc

from src.application import CatalogServiceImp


class CatalogServicer(catalog_pb2_grpc.CatalogServicer):
    def __init__(self):
        self.catalog = CatalogServiceImp()


    async def CreateProduct(self, request, context):
        return await self.catalog.CreateProduct(request, context)


    async def UpdateProduct(self, request, context):
        return await self.catalog.UpdateProduct(request, context)


    async def DeleteProduct(self, request, context):
        return await self.catalog.DeleteProduct(request, context)


    async def GetAllProducts(self, request, context):
        return await self.catalog.GetAllProducts(request, context)


    async def GetProductByName(self, request, context):
        return await self.catalog.GetProductByName(request, context)


    async def GetProductByID(self, request, context):
        return await self.catalog.GetProductByID(request, context)


    async def GetProductByCategory(self, request, context):
        return await self.catalog.GetProductByCategory(request, context)


    async def AddReview(self, request, context):
        return await self.catalog.AddReview(request, context)