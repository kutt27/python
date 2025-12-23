"""
Pydantic: Computed Fields
==========================

Topic: @computed_field decorator

Real-World Applications:
- API responses needing calculated values
- Full name from first/last
- SEO slugs generated from titles
"""

from pydantic import BaseModel, computed_field

class Employee(BaseModel):
    first_name: str
    last_name: str
    salary: float
    bonus_pct: float = 0.10
    
    @computed_field
    @property
    def full_name(self) -> str:
        """Dynamically includes full_name in serialization."""
        return f"{self.first_name} {self.last_name}"
    
    @computed_field
    @property
    def total_compensation(self) -> float:
        """Calculates total comp."""
        return self.salary * (1 + self.bonus_pct)


def main():
    """Demonstrates computed fields."""
    print("="*70)
    print("COMPUTED FIELDS".center(70))
    print("="*70)
    
    emp = Employee(first_name="John", last_name="Doe", salary=50000)
    
    print(f"Employee: {emp.first_name}")
    print(f"Access computed: {emp.full_name}")
    
    print("\n[Serialization]")
    # computed fields appear in dump/json!
    print(emp.model_dump_json(indent=2))
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• `@computed_field` adds property logic to JSON output")
    print("• Unlike standard `@property`, it is included in `model_dump()`")
    print("• Read-only by default (derived from other fields)")
    print("="*70)


if __name__ == "__main__":
    main()
