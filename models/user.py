from typing import Literal, Optional
from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    gender: Literal['male', 'female']
    status: Literal['active', 'inactive']
    is_student: Optional[bool] = None