
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from .routes import main_routes
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

app.include_router(
    main_routes.routers,
    prefix="/api",
    # dependencies=[Depends(get_token_header)],
)

@app.get("/")
def default_app():
    return {"description": "Welcome to Poetry FastAPI!"}
