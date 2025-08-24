from fastapi import APIRouter
from ..controllers.users_controllers import create_users_ctrl
from ..validations.create_user import Usercreate

routers = APIRouter()


@routers.post("/")
def create_users(user_request: Usercreate):
    response = create_users_ctrl(user_request)
    return response
