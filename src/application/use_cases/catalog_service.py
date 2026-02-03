from proto import catalog_pb2
from src.config.database.repositories.product_repositories import MongoDBProductRepositiry
from src.utils.convert import (
    convert_create_product,
    convert_update_product,
    convert_from_Dict_to_Struct, 
    convert_add_review
)

from google.protobuf.struct_pb2 import Struct
from typing import Dict


class CatalogServiceImp():
    def __init__(self):
        self.repo = MongoDBProductRepositiry()


    async def CreateProduct(self, request, context) -> catalog_pb2.Okey:
        product = convert_create_product(request)
        
        await self.repo.create_product(product, context)

        return catalog_pb2.Okey


    async def UpdateProduct(self, request, context) -> catalog_pb2.Okey:
        product = convert_update_product(request)

        await self.repo.update_product(request.product_id, product, context)

        return catalog_pb2.Okey


    async def DeleteProduct(self, request, context)-> catalog_pb2.Okey:
        await self.repo.delete_product(request.product_id, context)

        return catalog_pb2.Okey


    async def GetAllProducts(self, request, context) -> catalog_pb2.GetAllProductsResponse:
        if request.limit >= 1:
            products_dict = await self.repo.get_all_products(limit= request.limit, context=context)
        else:
            products_dict = await self.repo.get_all_products(limit= 10, context=context)
        
        products_struct_list = []
        if products_dict:
            for product in products_dict:
                product_struct = convert_from_Dict_to_Struct(product)
                products_struct_list.append(product_struct)
            
        return catalog_pb2.GetAllProductsResponse(data= products_struct_list)


    async def GetProductByName(self, request, context) -> catalog_pb2.GetProductByNameResponse:
        product = await self.repo.get_product_by_name(product_name= request.product_nam, context=context)
        product_struct = convert_from_Dict_to_Struct(product)
        return catalog_pb2.GetProductByNameResponse(data=product_struct)


    async def GetProductByID(self, request, context) -> catalog_pb2.GetProductByIDResponse:
        product = await self.repo.get_product_by_id(product_id=request.product_id, context=context)
        if product:
            pruduct_reviews = await self.repo.get_reviews(product["reviews_id"], context=context)
            product_dict = product | pruduct_reviews
            product_struct = convert_from_Dict_to_Struct(product_dict)

            return catalog_pb2.GetProductByIDResponse(data=product_struct)


    async def GetProductByCategory(self,request, context) -> catalog_pb2.GetProductByCategoryResponse:
        products_dict = await self.repo.get_product_by_category(product_category=request.product_category, context=context)
        products_struct_list = []
        if products_dict:
            for product in products_dict:
                product_struct = convert_from_Dict_to_Struct(product)
                products_struct_list.append(product_struct)
        return catalog_pb2.GetProductByCategoryResponse(data= products_struct_list)


    async def AddReview(self,request, context)->catalog_pb2.Okey:
        review = convert_add_review(request)
        await self.repo.add_review(request.review_id, review, context)


    





