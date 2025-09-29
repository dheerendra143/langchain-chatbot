from pydantic import BaseModel, Field


class Usercreate(BaseModel):
    username: str =  Field(min_length=1, max_length=50)
    email: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8, max_length=20)