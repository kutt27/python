"""
Topic: Computed Fields.

Use `@computed_field` to include evaluated properties dynamically 
in your serialized output (`model_dump` and `model_dump_json`).
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
        return f"{self.first_name} {self.last_name}"
    
    @computed_field
    @property
    def total_compensation(self) -> float:
        return self.salary * (1 + self.bonus_pct)

if __name__ == "__main__":
    emp = Employee(first_name="John", last_name="Doe", salary=50000)
    print("Computed Field Serialization:")
    print(emp.model_dump_json(indent=2))
