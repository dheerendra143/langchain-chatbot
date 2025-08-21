from fastapi import APIRouter
from poetry_fastapi.src.apiDoc.users import getAllUser
userRouter = APIRouter()



@userRouter.get("/", **getAllUser.swaggerUserConfigDict)
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@userRouter.get("/{username}")
async def read_user(username: str):
    return {"username": username}