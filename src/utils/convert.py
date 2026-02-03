from proto import catalog_pb2
from application.dtos import *
from utils.time import get_utc_now

from bson import ObjectId
from google.protobuf.struct_pb2 import Struct
from typing import Dict, List
from google.protobuf.json_format import MessageToDict, ParseDict

def convert_create_product(request)->ProductCreateDTO:
    create_time = get_utc_now()
    return ProductCreateDTO(id= request.id , name= request.name, description = request.description, price= request.price, category= request.category, create_time= create_time)


def convert_update_product(request)->ProductUpdateDTO:
    try:
        reviews_id= ObjectId(request.reviews_id)
    except:
        reviews_id = ObjectId()

    return ProductUpdateDTO(id=request.product_id, name = request.name, description=request.description, price= request.price,category= request. category, reviews_id=reviews_id )


def convert_add_review(request)->ReviewDTO:
    review_dict = {
        "id": request.id,
        "user_id": request.user_id,
        "rating": request.rating,
        "text": request.text
    }

    return ReviewDTO(**review_dict)


def convert_from_Struct_to_Dict(struct:Struct)->Dict:
    data_dict = MessageToDict(struct)

    return data_dict

def convert_from_Dict_to_Struct(dict:Dict)->Struct:
    data_struct = Struct()
    ParseDict(dict, data_struct)

    return data_struct


def from_listStruct_to_listDict(list:List[Struct])->List[Dict]:
    list_of_Dict = []
    for struct in list:
        new_dict = MessageToDict(struct)
        list_of_Dict.append(new_dict)
    return list_of_Dict
