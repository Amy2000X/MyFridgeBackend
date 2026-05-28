from pydantic import BaseModel
from typing import Optional

class RegisterRequest(BaseModel):
    email: str
    password: str
    
    # class Config:
    #     from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str