from pydantic import BaseModel, HttpUrl


class UserDataSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class SupportSchema(BaseModel):
    url: HttpUrl
    text: str


class UserSchema(BaseModel):
    data: UserDataSchema
    support: SupportSchema
