from poetry_fastapi.src.modules.users.routes import usersRoutes

from fastapi import APIRouter

mainRouter = APIRouter()

mainRouter.include_router(
    usersRoutes.userRouter,
    prefix="/users",
    tags=["Users"]
);