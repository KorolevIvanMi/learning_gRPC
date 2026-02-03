from proto import catalog_pb2



from bson import ObjectId
from google.protobuf.struct_pb2 import Struct
from typing import Dict, List
from google.protobuf.json_format import MessageToDict, ParseDict

def convert_create_product(request):
    from src.application.dtos import ProductCreateDTO
    
    return ProductCreateDTO(id= request.id , name= request.name, description = request.description, price= request.price, category= request.category)


def convert_update_product(request):
    from src.application.dtos import  ProductUpdateDTO
    try:
        reviews_id= ObjectId(request.reviews_id)
    except:
        reviews_id = ObjectId()

    return ProductUpdateDTO(id=request.product_id, name = request.name, description=request.description, price= request.price,category= request. category, reviews_id=reviews_id )


def convert_add_review(request):
    from src.application.dtos import  ReviewDTO
    review_dict = {
        "id": request.id,
        "user_id": request.user_id,
        "rating": request.rating,
        "text": request.text
    }

    return ReviewDTO(**review_dict)


def convert_from_Struct_to_Dict(struct:Struct)->Dict:
    return dict(struct)

def convert_from_Dict_to_Struct(dict:Dict)->Struct:
    data_struct = Struct()
    ParseDict(dict, data_struct)
    return data_struct



def from_listStruct_to_listDict(response: catalog_pb2.GetAllProductsResponse) -> List[Dict]:
    """Convert GetAllProductsResponse to list of dicts"""
    list_of_Dict = []
    for struct in response.data:  # ← response.data, а не сам response
        new_dict = dict(struct)  # Struct в protobuf 6.x ведет себя как dict
        list_of_Dict.append(new_dict)
    return list_of_Dict
