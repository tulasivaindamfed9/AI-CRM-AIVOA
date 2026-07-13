from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

    
class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    date: str
    time: str
    attendees: str
    topics_discussed: str
    materials_shared: str
    samples_distributed: str
    sentiment: str
    outcomes: str
    follow_up_actions: str
    ai_suggestions: str


class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        from_attributes = True


class EditRequest(BaseModel):
    message: str        