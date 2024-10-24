from pydantic import BaseModel, ConfigDict

class TodoDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    completed: bool
    day: int