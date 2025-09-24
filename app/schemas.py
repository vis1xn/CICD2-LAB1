# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint
class User(BaseModel):
 user_id: int
 student_id: constr(regex='^S.*$')
 name: constr(min_length=2, max_length=50)
 email: EmailStr
 age: conint(gt=18)