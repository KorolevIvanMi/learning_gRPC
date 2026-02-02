from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductRequest(_message.Message):
    __slots__ = ("id", "name", "description", "price", "category")
    class DescriptionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: _containers.ScalarMap[str, str]
    price: int
    category: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Mapping[str, str]] = ..., price: _Optional[int] = ..., category: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateProductRequest(_message.Message):
    __slots__ = ("product_id", "name", "description", "price", "category", "reviews_id")
    class DescriptionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    name: str
    description: _containers.ScalarMap[str, str]
    price: int
    category: _containers.RepeatedScalarFieldContainer[str]
    reviews_id: str
    def __init__(self, product_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Mapping[str, str]] = ..., price: _Optional[int] = ..., category: _Optional[_Iterable[str]] = ..., reviews_id: _Optional[str] = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetAllProductsRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class GetAllProductsResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class GetProductByNameRequest(_message.Message):
    __slots__ = ("product_name",)
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    def __init__(self, product_name: _Optional[str] = ...) -> None: ...

class GetProductByNameResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _struct_pb2.Struct
    def __init__(self, data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GetProductByIDRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetProductByIDResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _struct_pb2.Struct
    def __init__(self, data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GetProductByCategoryRequest(_message.Message):
    __slots__ = ("product_category",)
    PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    product_category: str
    def __init__(self, product_category: _Optional[str] = ...) -> None: ...

class GetProductByCategoryResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class AddReviewRequest(_message.Message):
    __slots__ = ("review_id", "id", "user_id", "rating", "text")
    REVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    review_id: str
    id: int
    user_id: int
    rating: float
    text: str
    def __init__(self, review_id: _Optional[str] = ..., id: _Optional[int] = ..., user_id: _Optional[int] = ..., rating: _Optional[float] = ..., text: _Optional[str] = ...) -> None: ...

class Okey(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
