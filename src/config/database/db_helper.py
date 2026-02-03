from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
from contextlib import asynccontextmanager

from src.config.config import settings


class MongoDB:
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None


    @classmethod
    async def connect(cls):
        try:
            cls.client = AsyncIOMotorClient(settings.mongodb_url)
            await cls.client.admin.command('ping')

            cls.database = cls.client[settings.mongo_base_name]

            print("MongoDB connected")
        
        except Exception as e:
            print(f"Connection error: {e}")

            raise


    @classmethod
    async def disconnect(cls):
        if cls.client:
            cls.client.close()
            
            print("MongoDB disconnected")

            
db_helper = MongoDB()

