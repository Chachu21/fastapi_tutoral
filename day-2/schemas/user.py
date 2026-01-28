from pydantic import BaseModel, EmailStr
from datetime import datetime

# -------------------------
# Request schema (for creating/updating a user)
# -------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

# -------------------------
# Response schema (what we return to client)
# -------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # allows SQLAlchemy models to be automatically converted
