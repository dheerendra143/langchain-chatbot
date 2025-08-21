
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .modules.users.routes import usersRoutes
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

app.include_router(
    usersRoutes.userRouter,
    prefix="/users",
    tags=["Users"],
    # dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

