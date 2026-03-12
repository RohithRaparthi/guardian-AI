from pydantic import BaseModel


class GuardianCreate(BaseModel):
    name: str
    email: str


class GuardianResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True