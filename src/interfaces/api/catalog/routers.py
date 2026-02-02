import grpc
import asyncio
from fastapi import APIRouter, HTTPException
from google.protobuf.json_format import MessageToDict

from proto import catalog_pb2, catalog_pb2_grpc

