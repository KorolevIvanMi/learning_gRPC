from fastapi import APIRouter, Depends, HTTPException, status

from core.gRPC.client.grpc_client import grpc_client
from proto import catalog_pb2
from config.config import settings
from src.utils import from_listStruct_to_listDict, convert_from_Struct_to_Dict
from application.dtos import ProductCreateDTO
from utils import get_utc_now


router = APIRouter(tags=["Catalog"])

@router.get("/")
async def get_products(limint:int):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        request = catalog_pb2.GetAllProductsRequest(limit=limint)
        response = await stub.GetAllProducts(request)
        response = from_listStruct_to_listDict(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{product_name}/")
async def get_product_by_name(product_name:str):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        request = catalog_pb2.GetProductByNameRequest(product_name=product_name)
        response = await stub.GetProductByName(request)
        response = convert_from_Struct_to_Dict(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{product_id}/")
async def get_product_by_id(product_id:str):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        request = catalog_pb2.GetProductByIDRequest(product_id=product_id)
        response = await stub.GetProductByID(request)
        response = convert_from_Struct_to_Dict(response)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=ProductCreateDTO,  status_code= status.HTTP_201_CREATED,)
async def create_product(product_in:ProductCreateDTO):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        request = catalog_pb2.CreateProductRequest(id=product_in.id, name=product_in.name, description = product_in.description, price= product_in.price, category=product_in.category)
        response = await stub.CreateProduct(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))