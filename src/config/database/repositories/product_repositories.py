import grpc
from typing import List, Dict
from bson import ObjectId

from database.db_helper import db_helper
from application.dtos import *
from .iaproduct_repositories import IAMongoDBProductRepositiry
from utils import get_utc_now


class MongoDBProductRepositiry(IAMongoDBProductRepositiry):
    async def create_product(self, product: ProductCreateDTO, context) -> None:
        try:
            async with db_helper.transaction() as session:

                review_id = ObjectId()
                
                product_data = product.model_dump() 
                product_data['review_id'] = review_id
                
                await db_helper.database.products.insert_one(
                    product_data,
                    session=session
                )

                await db_helper.database.reviews.insert_one({
                    "id": review_id,
                    "reviews": []},
                session=session)

        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def update_product(self,product_id: str, product:ProductUpdateDTO, context)->None:
        try: 
            update_data = product.model_dump(exclude_none=True)
            update_data["updated_time"] = get_utc_now()

            async with db_helper.transaction() as session:

                await db_helper.database.products.update_one(
                    {"id": product_id}, 
                    {"$set": update_data},
                    session=session
                )
            
                # updated = await db_helper.database.products.find_one(
                #     {"id": product_id}, session = session
                # )

                # return ProductBaseDTO(**updated)
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def delete_product(self, product_id:str, context):
        try:
            
            async with db_helper.transaction() as session:
                deleted_product = db_helper.database.products.find_one(
                    {"id": product_id}, session = session
                )
                reviews_to_del = deleted_product["review_id"]

                await db_helper.database.products.delete_one({"id":product_id}, session=session)
                await db_helper.database.reviews.delete_one({"id":reviews_to_del}, session=session)


        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_reviews(self, reviews_id: ObjectId , context)->ReviewDictDTO:
        try:
            async with db_helper.transaction() as session:
                result = await db_helper.database.reviews.find_one({"id":reviews_id}, session = session)
                
                return  await ReviewDictDTO(**result)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_all_products(self, limit,context)->List[Dict]|None:
        try:
            async with db_helper.transaction() as session:
                cursor = await db_helper.database.products.find(session=session).limit(limit)

                result = await cursor.to_list(length=limit)

                return result
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_name(self, product_name:str, context)->Dict|None:
        try:
            async with db_helper.transaction() as session:
                product = await db_helper.database.products.find_one({"name":product_name}, session=session)
                
                return product
            
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_id(self, product_id:str, context)->Dict|None:
        try:
            async with db_helper.transaction() as session:
                product = await db_helper.database.products.find_one({"id":product_id}, session = session)
                
                return product
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_category(self, product_category:str, context):
        try:
            async with db_helper.transaction() as session:
                cursor = await db_helper.database.products.find({"category" : product_category}, session= session)
                products = await cursor.to_list(length=None)
                return products
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def add_review(self, review_id:ObjectId, review: ReviewDTO, context):
        try:
            async with db_helper.transaction() as session:
                await db_helper.database.reviews.update_one(
                    {"id": review_id},
                    {"$push": {"reviews": review}}, session=session)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
