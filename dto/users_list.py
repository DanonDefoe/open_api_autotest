from pydantic import BaseModel


class UsersData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersSupport(BaseModel):
    url: str
    text: str


class ListUsersSchema(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: UsersData
    support: UsersSupport
