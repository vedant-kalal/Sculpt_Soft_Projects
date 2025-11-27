from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True # This is used to convert the database model to a pydantic model

class Token(BaseModel):
    access_token: str
    token_type: str     



    
