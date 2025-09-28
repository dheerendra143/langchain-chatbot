from langchain_ollama.src.model.response import users

swaggerUserConfigDict = {
    "include_in_schema": True,
    "summary": "Api to get all users",
    "description":"This api is a get api to fetch the all users",
    "name": "getAllUser",
    # "response_model": users.User
}