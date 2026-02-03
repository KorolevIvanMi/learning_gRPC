from fastapi import APIRouter, Depends, HTTPException, status
from google.protobuf.json_format import ParseDict

from src.core.gRPC.client.grpc_client import grpc_client
from proto import catalog_pb2
from src.config.config import settings
from src.utils.convert import from_listStruct_to_listDict, convert_from_Struct_to_Dict
from src.application.dtos import ProductCreateDTO
from src.utils.time import get_utc_now
from google.protobuf.json_format import MessageToDict

router = APIRouter(tags=["Catalog"])

@router.get("/")
async def get_products(limit: int):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        
        request = catalog_pb2.GetAllProductsRequest(limit=limit)
        proto_response = await stub.GetAllProducts(request)
        
        response_dict = MessageToDict(
            proto_response,
            preserving_proto_field_name=True,
            use_integers_for_enums=True
        )
        
        return response_dict
        
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

@router.post("/",  status_code= status.HTTP_201_CREATED,)
async def create_product(product_in:ProductCreateDTO):
    try:
        stub = grpc_client.get_stub()
        if not stub:
            await grpc_client.connect()
            stub = grpc_client.get_stub()
        product_dict = product_in.model_dump()
        
        request = catalog_pb2.CreateProductRequest()
        request = ParseDict(product_dict, request)
        response = await stub.CreateProduct(request)
        response_dict = MessageToDict(response)
        
        return response_dict 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))