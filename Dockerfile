FROM python:3.13-slim

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry==2.2.1
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости
RUN poetry install --no-root

# Копируем весь код приложения
COPY . .

# Генерируем protobuf файлы (важно сделать это в контейнере)
RUN python -m grpc_tools.protoc \
    -I./proto \
    --python_out=./proto \
    --grpc_python_out=./proto \
    ./proto/catalog_service/catalog.proto

# Исправляем импорты в сгенерированном файле
RUN sed -i 's/import catalog_pb2 as catalog__pb2/from . import catalog_pb2 as catalog__pb2/' \
    proto/catalog_service/generated/catalog_pb2_grpc.py

# Открываем порты
EXPOSE 8000   
EXPOSE 50051  

# Запускаем приложение (и gRPC и FastAPI вместе)
CMD ["python", "main.py"]