from pydantic import BaseModel

class Complaint(BaseModel):
    title: str
    description: str
    category: str
    location: str
    user_id: int
    
class StatusUpdate(BaseModel):
    status: str