from pydantic import BaseModel, Field

class Notification(BaseModel):
    title:str
    body:str