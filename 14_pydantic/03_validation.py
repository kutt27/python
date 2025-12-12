"""
Pydantic: Validators (V2)
==========================

Topic: @field_validator and @model_validator

Real-World Applications:
- Cross-field validation (password confirmation)
- Custom format checks
- Business logic validation
"""

from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo
from datetime import date, timedelta

class Booking(BaseModel):
    """Hotel booking model."""
    guest_name: str
    check_in: date
    check_out: date
    num_guests: int = Field(gt=0)
    
    # 1. Field Validator: Checks single field
    @field_validator('check_in')
    @classmethod
    def check_in_future(cls, v: date) -> date:
        if v < date.today():
            raise ValueError("Check-in date cannot be in the past")
        return v
    
    # 2. Model Validator: Checks multiple fields (After validation of types)
    @model_validator(mode='after')
    def check_dates_order(self) -> 'Booking':
        if self.check_out <= self.check_in:
            raise ValueError("Check-out must be after check-in")
            
        stay_duration = (self.check_out - self.check_in).days
        if stay_duration > 30:
            raise ValueError("Maximum stat duration is 30 days")
            
        return self


def main():
    """Demonstrates validators."""
    print("="*70)
    print("CUSTOM VALIDATORS".center(70))
    print("="*70)
    
    today = date.today()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    
    print("\n[1] Field Validation (Past Date)")
    try:
        Booking(
            guest_name="Bob",
            check_in=yesterday,
            check_out=tomorrow,
            num_guests=1
        )
    except Exception as e:
        print(f"✗ Error: {e}")
        
    print("\n[2] Model Validation (Check-out before Check-in)")
    try:
        Booking(
            guest_name="Alice",
            check_in=tomorrow,
            check_out=today, # Wrong order
            num_guests=1
        )
    except Exception as e:
        print(f"✗ Error: {e}")
        
    print("\n[3] Valid Booking")
    booking = Booking(
        guest_name="Charlie",
        check_in=today,
        check_out=today + timedelta(days=5),
        num_guests=2
    )
    print(f"✓ Booking Confirmed: {booking}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• `@field_validator('field')`: Validates individual fields")
    print("• `@model_validator(mode='after')`: Validates whole model (cross-field)")
    print("• Raise `ValueError` or `AssertionError` to fail validation")
    print("="*70)


if __name__ == "__main__":
    main()
