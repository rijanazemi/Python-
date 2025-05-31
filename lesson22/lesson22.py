from pydantic import BaseModel, conint, constr
from typing_extensions import Optional


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


user = User(id=1, name='John', age="23", email='john@example.com')

print(user)


class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None


user2 = User(id=1, name='John', age=25)

user3 = User(id=1, name='John', email='john@example.com')

print(user3)

class another_user(BaseModel):
    id: conint(gt=0)
    name: coinstr(min_length=2, max_length=50)

valid_user = another_user(id=1, name='John')
print(valid_user)

valid_user1 = another_user(id=0, name='John')
print(valid_user1)
