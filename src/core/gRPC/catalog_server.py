from proto import catalog_pb2_grpc

from src.application import CatalogServiceImp


class CatalogServicer(catalog_pb2_grpc.CatalogServicer):
    async def CreateProduct(self, request, context):
        return await CatalogServiceImp().CreateProduct(request, context)


    async def UpdateProduct(self, request, context):
        return await CatalogServiceImp().UpdateProduct(request, context)


    async def DeleteProduct(self, request, context):
        return await CatalogServiceImp().DeleteProduct(request, context)


    async def GetAllProducts(self, request, context):
        return await CatalogServiceImp().GetAllProducts(request, context)


    async def GetProductByName(self, request, context):
        return await CatalogServiceImp().GetProductByName(request, context)


    async def GetProductByID(self, request, context):
        return await CatalogServiceImp().GetProductByID(request, context)


    async def GetProductByCategory(self, request, context):
        return await CatalogServiceImp().GetProductByCategory(request, context)


    async def AddReview(self, request, context):
        return await CatalogServiceImp().AddReview(request, context)