from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    last_name: str
    age: int
    adress: str
    email: EmailStr
 
 
class UserCreate(BaseModel):
   password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True