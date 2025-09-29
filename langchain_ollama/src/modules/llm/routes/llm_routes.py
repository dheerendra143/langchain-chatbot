from fastapi import APIRouter
from starlette import status

from ..controllers.llm_controllers import create_users_ctrl
from ..validations.create_user import Usercreate

from langchain_ollama.src.llm.gemma2.index import chain
from langchain_ollama.src.modules.llm.models import llm


routers = APIRouter()

ollama_api_url = "http://localhost:11434/api/generate"



@routers.post("/generate", status_code= status.HTTP_200_OK)
def create_llm(request: llm.PromptRequest):
    response = chain.invoke({"input": request.prompt})
    return {"response": response}


@routers.post("/", status_code= status.HTTP_201_CREATED)
def create_users(user_request: Usercreate):
    response = create_users_ctrl(user_request)
    return response
