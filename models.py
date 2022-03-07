from pydantic import BaseModel

class Message(BaseModel):
    channel: str
    author: str
    text: str