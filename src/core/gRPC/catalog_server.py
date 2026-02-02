from proto import catalog_pb2_grpc

from application import CatalgoServiceImp


class CatalogServicer(catalog_pb2_grpc.CatologServicer):
    async def CreateProduct(self, request, context):
        return await CatalgoServiceImp.CreateProduct(request, context)


    async def UpdateProduct(self, request, context):
        return await CatalgoServiceImp.UpdateProduct(request, context)


    async def DeleteProduct(self, request, context):
        return await CatalgoServiceImp.DeleteProduct(request, context)


    async def GetAllProducts(self, request, context):
        return await CatalgoServiceImp.GetAllProducts(request, context)


    async def GetProductByName(self, request, context):
        return await CatalgoServiceImp.GetProductByName(request, context)


    async def GetProductByID(self, request, context):
        return await CatalgoServiceImp.GetProductByID(request, context)


    async def GetProductByCategory(self, request, context):
        return await CatalgoServiceImp.GetProductByCategory(request, context)


    async def AddReview(self, request, context):
        return await CatalgoServiceImp.AddReview(request, context)