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
    struct = Struct()
    struct.update(dict)
    return struct



def from_listStruct_to_listDict(list:List[Struct])->List[Dict]:
    return [dict(struct) for struct in list]
