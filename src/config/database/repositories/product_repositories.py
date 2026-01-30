import grpc

from database.db_helper import db_helper
from application.dtos import *
from .iaproduct_repositories import IAMongoDBProductRepositiry
from utils import get_utc_now

class MongoDBProductRepositiry(IAMongoDBProductRepositiry):
    async def create_product(self, product: ProductCreateDTO, context) -> None:
        try:
            async with db_helper.transaction() as session:
                await db_helper.database.products.insert_one(product, session= session)
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))


    async def update_product(self,product_id: str, product:ProductUpdateDTO, context)->ProductBaseDTO:
        try: 
            update_data = product.model_dump(exclude_none=True)
            update_data["updated_time"] = get_utc_now()

            async with db_helper.transaction() as session:

                await db_helper.database.products.update_one(
                    {"id": product_id}, 
                    {"$set": update_data},
                    session=session
                )
            
                updated = await db_helper.database.products.find_one(
                    {"id": product_id}, session = session
                )

                return ProductBaseDTO(**updated)
        except Exception as e:
            await context.abort(grpc.StatusCode.INTERNAL, str(e))
        
        



