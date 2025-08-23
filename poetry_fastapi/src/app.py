
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from .routes import mainRoutes
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
)

app.include_router(
    mainRoutes.mainRouter,
    prefix="/api",
    # dependencies=[Depends(get_token_header)],
)

@app.get("/")
def default_app():
    return {"description": "Welcome to Poetry FastAPI!"}
