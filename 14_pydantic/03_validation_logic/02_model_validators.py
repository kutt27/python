"""
Topic: Model Validators.

Use `@model_validator` when you need to validate fields across 
the entirety of the model or cross-check different attributes.
"""

from pydantic import BaseModel, model_validator
from datetime import date, timedelta

class Reservation(BaseModel):
    check_in: date
    check_out: date

    # mode='after' means it runs after individual field validation
    @model_validator(mode='after')
    def validate_dates(self) -> 'Reservation':
        if self.check_out <= self.check_in:
            raise ValueError("Check-out must be after check-in")
        
        duration = (self.check_out - self.check_in).days
        if duration > 30:
            raise ValueError("Max duration is 30 days")
        
        return self

if __name__ == "__main__":
    try:
        # Fails cross-field check
        Reservation(
            check_in=date.today(),
            check_out=date.today()
        )
    except Exception as e:
        print(f"Error: {e}")
