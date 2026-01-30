from abc import ABC, abstractmethod
from typing import List, Dict
from bson import ObjectId 

from application.dtos import *


class IAMongoDBProductRepositiry(ABC):
    @abstractmethod
    async def create_product(
        self,
        product: ProductCreateDTO,
        context
    ) -> None:
        pass


    @abstractmethod
    async def update_product(
        self,
        product_id: str,
        product: ProductUpdateDTO,
        context
    ) -> ProductUpdateDTO:
        pass


    @abstractmethod
    async def delete_product(
        self, 
        product_id: str,
        context
    )-> None:
        pass


    @abstractmethod
    async def get_all_products(
        self,
        limit:int, 
        context
    )->List[Dict]:
        pass


    @abstractmethod
    async def get_product_by_name(
        self,
        product_name:str,
        context
    )->Dict|None:
        pass


    @abstractmethod
    async def get_product_by_id(
        self, 
        product_id:str,
        context
    )->Dict|None:
        pass


    @abstractmethod
    async def get_product_by_category(
            self, 
            product_category: str,
            context
    )-> List[Dict]|None:
        pass


    # @abstractmethod
    # async def get_product_by_price(
    #     self,
    #     product_price: float,
    #     context
    # )->List[Dict]|None:
    #     pass


    @abstractmethod
    async def add_review(
        self, 
        review_id: ObjectId,
        review: ReviewDTO,
        context
    ):
        pass


    @abstractmethod
    async def get_review(
        self,
        review_id: int,
        context
    )->ReviewDictDTO:
        pass