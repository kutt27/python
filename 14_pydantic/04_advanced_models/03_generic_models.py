"""
Topic: Generic Models.

Inherit from `Generic[T]` to create reusable envelopes or 
templates for your data. Very useful in APIs.
"""

from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    status: str
    data: T
    meta: dict = {}

class User(BaseModel):
    name: str

if __name__ == "__main__":
    # Wrap a single User
    user = User(name="Alice")
    res1 = APIResponse[User](status="success", data=user)
    print(f"Single User Request: {res1.data.name}")

    # Wrap a List of Users
    users = [User(name="Bob"), User(name="Charlie")]
    res2 = APIResponse[List[User]](status="success", data=users)
    print(f"Multiple Users Request length: {len(res2.data)}")
