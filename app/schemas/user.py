from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=4, max_length=72)

class UserRead(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True