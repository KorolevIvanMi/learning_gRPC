import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    app_name:str = "gRPC_fastapi_app"

    app_prefix:str = "/grpc_fastapi"

    mongo_user:str = os.getenv("MONGODB_USER_LOGIN")
    mongo_password:str = os.getenv("MONGODB_USER_PASSWORD")
    mongo_base_name: str = os.getenv("MONGODB_DATABASE_NAME")

    mongodb_url:str = ""


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mongodb_url = (
        f"mongodb://{self.mongo_user}:{self.mongo_password}"
        f"@mongodb:27017/{self.mongo_base_name}"
        f"?authSource={self.mongo_base_name}" )


settings = Settings()