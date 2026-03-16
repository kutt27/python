"""
Topic: Field Validators.

You can create custom validation logic for individual fields 
using the `@field_validator` decorator.
"""

from pydantic import BaseModel, field_validator
from datetime import date, timedelta

class Booking(BaseModel):
    guest_name: str
    check_in: date

    # Ensure check-in date is not in the past
    @field_validator('check_in')
    @classmethod
    # Pydantic V2 passes 'cls' to the validator implicitly
    def check_in_future(cls, v: date) -> date:
        if v < date.today():
            raise ValueError("Check-in date cannot be in the past")
        return v

if __name__ == "__main__":
    today = date.today()
    past_date = today - timedelta(days=5)

    try:
        Booking(guest_name="Alice", check_in=past_date)
    except Exception as e:
        print(f"Error: {e}")
