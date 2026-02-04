import grpc
from typing import List, Dict
from bson import ObjectId

from src.config.database.db_helper import db_helper
from src.application.dtos import *
from .iaproduct_repositories import IAMongoDBProductRepositiry
from src.utils.time import get_utc_now


class MongoDBProductRepositiry(IAMongoDBProductRepositiry):
    async def create_product(self, product: ProductCreateDTO, context) -> None:
        try:
            review_id = ObjectId()
            
            product_data = product.model_dump() 
            product_data['review_id'] = review_id
            
            
            await db_helper.database.reviews.insert_one({
                "_id": review_id,
                "collection_id": review_id,
                "reviews": [], 
                
            })
            await db_helper.database.products.insert_one(product_data)

        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def update_product(self, product_id: str, product: ProductUpdateDTO, context) -> None:
        try: 
            update_data = product.model_dump(exclude_none=True)
            await db_helper.database.products.update_one(
                {"id": product_id}, 
                {"$set": update_data}
            )
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def delete_product(self, product_id: str, context):
        try:
            deleted_product = await db_helper.database.products.find_one({"id": product_id})
            if deleted_product:
                reviews_to_del = deleted_product.get("review_id")
                await db_helper.database.products.delete_one({"id": product_id})
                if reviews_to_del:
                    await db_helper.database.reviews.delete_one({"collection_id": reviews_to_del})
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_reviews(self, reviews_id: ObjectId, context) -> Dict:
        try:
            result = await db_helper.database.reviews.find_one({"collection_id": reviews_id},{"_id": 0})
            result["collection_id"] = str(result["collection_id"])
            return result
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_all_products(self, limit, context) -> List[Dict] | None:
        try:
            cursor = db_helper.database.products.find(
            {}, 
            {"_id": 0}  
            ).limit(limit)
        
            result = await cursor.to_list(length=limit)
            
            # Конвертируем ObjectId в строки
            for product in result:
                if "review_id" in product and product["review_id"]:
                    product["review_id"] = str(product["review_id"])
            
            return result
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_name(self, product_name: str, context) -> Dict | None:
        try:
            product = await db_helper.database.products.find_one({"name": product_name},{"_id": 0})
            product["review_id"] = str(product["review_id"])
            return product
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_id(self, product_id: str, context) -> Dict | None:
        try:
            product = await db_helper.database.products.find_one({"id": product_id},{"_id": 0})
            product["review_id"] = str(product["review_id"])
            return product
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def get_product_by_category(self, product_category: str, context):
        try:
            cursor = db_helper.database.products.find({"category": product_category}, {"_id": 0})

            products = await cursor.to_list(length=None)
            for product in products:
                if "review_id" in product and product["review_id"]:
                    product["review_id"] = str(product["review_id"])
            return products
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def add_review(self, review_id: ObjectId, review:ReviewDTO, context):
        try:
            await db_helper.database.reviews.update_one(
                {"collection_id": review_id},
                {"$push": {"reviews": review}}
            )
            
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))