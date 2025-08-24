from fastapi import APIRouter
from starlette import status

from ..controllers.users_controllers import create_users_ctrl
from ..validations.create_user import Usercreate

routers = APIRouter()


@routers.post("/", status_code= status.HTTP_201_CREATED)
def create_users(user_request: Usercreate):
    response = create_users_ctrl(user_request)
    return response
