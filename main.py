import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from src.config.database.db_helper import db_helper
from src.config.config import settings
from src.interfaces.api.catalog.routers import router as catalog_router
from src.core.gRPC.server.grpc_server import GRPCServer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_helper.connect()
    print("MongoDB connected!")

    grpc_server = GRPCServer(port = 50051)
    grpc_task = asyncio.create_task(grpc_server.serve_forever())
    app.state.grpc_task = grpc_task
    app.state.grpc_server = grpc_server

    yield
    if hasattr(app.state, 'grpc_server'):
        await app.state.grpc_server.stop()
        print("gRPC сервер остановлен")
    
    # Отменяем задачу
    if hasattr(app.state, 'grpc_task'):
        app.state.grpc_task.cancel()
    await db_helper.disconnect()

app = FastAPI(
    lifespan=lifespan
)

app.include_router(router=catalog_router, prefix=settings.app_prefix)

@app.get("/")
def root():
    return {
        "message": "Добро пожаловать!",
        "services": ["mongodb", "grpc", "rest"],
        "docs": "/docs"
    }

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # ← ДОЛЖНО БЫТЬ 0.0.0.0, а не 127.0.0.1
        port=8000, 
        reload=True
    )