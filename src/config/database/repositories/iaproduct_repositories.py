from abc import ABC, abstractmethod
from typing import List, Dict

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
        limit:int = 100
    )->List[Dict]:
        pass


    @abstractmethod
    async def get_product_by_name(
        self,
        product_name:str,
        context
    )->ProductBaseDTO|None:
        pass


    @abstractmethod
    async def get_product_by_id(
        self, 
        product_id:str,
        context
    )->ProductBaseDTO|None:
        pass


    @abstractmethod
    async def get_product_by_category(
            self, 
            product_category: str,
            context
    )-> List[ProductBaseDTO]|None:
        pass


    @abstractmethod
    async def get_product_by_price(
        self,
        product_price: float,
        context
    )->List[ProductBaseDTO]|None:
        pass


    
