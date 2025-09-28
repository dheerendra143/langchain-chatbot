from langchain_ollama.src.modules.users.routes import users_routes

from fastapi import APIRouter

routers = APIRouter()

routers.include_router(
    users_routes.routers,
    prefix="/v1/users",
    tags=["Users"]
);