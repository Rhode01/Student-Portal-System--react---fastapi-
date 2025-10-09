from pydantic import BaseModel
class UserSchema(BaseModel):
    email : str
    full_name : str
    is_active : bool
    username :str
    password : str
    role:str
class UserLoginSchema(BaseModel):
    username:str
    password:str