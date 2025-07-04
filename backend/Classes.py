from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class OurLocation(BaseModel):
    x : float 
    y : float

class GoogleLocation(BaseModel):
    x: float 
    y : float 
    name : str 
    address : str
    
class Admin (BaseModel):
    Name: str
    Email :str 
    EncrpyedPasswordEntered : str 
    
# using smtp to send the email and data implement it when you are working for it 
# place to upload photo to display 
    
    