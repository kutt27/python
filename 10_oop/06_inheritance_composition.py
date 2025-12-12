"""
Python OOP: Inheritance vs Composition
=======================================

Topic: IS-A vs HAS-A relationships, design patterns

Real-World Applications:
- Code reuse
- Design patterns
- Flexible architectures
"""


# Inheritance (IS-A relationship)
class Employee:
    """Base employee class."""
    
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id
    
    def get_info(self) -> str:
        return f"{self.name} (ID: {self.employee_id})"


class Manager(Employee):
    """Manager IS-A Employee."""
    
    def __init__(self, name: str, employee_id: int, department: str):
        super().__init__(name, employee_id)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee: Employee):
        self.team.append(employee)


# Composition (HAS-A relationship)
class Address:
    """Address component."""
    
    def __init__(self, street: str, city: str, zip_code: str):
        self.street = street
        self.city = city
        self.zip_code = zip_code
    
    def __str__(self):
        return f"{self.street}, {self.city} {self.zip_code}"


class Person:
    """Person HAS-A Address."""
    
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address  # Composition


def main():
    """Demonstrates inheritance vs composition."""
    print("="*70)
    print("INHERITANCE VS COMPOSITION".center(70))
    print("="*70)
    
    print("\n[1] INHERITANCE (IS-A)")
    print("-" * 70)
    
    emp = Employee("Alice", 101)
    manager = Manager("Bob", 201, "Engineering")
    
    print(f"Employee: {emp.get_info()}")
    print(f"Manager: {manager.get_info()}")
    print(f"Manager is Employee? {isinstance(manager, Employee)}")
    
    manager.add_team_member(emp)
    print(f"Team size: {len(manager.team)}")
    
    print("\n[2] COMPOSITION (HAS-A)")
    print("-" * 70)
    
    address = Address("123 Main St", "NYC", "10001")
    person = Person("Charlie", address)
    
    print(f"{person.name} lives at: {person.address}")
    
    print("\n" + "="*70)
    print("When to Use:")
    print("Inheritance (IS-A):")
    print("  • Subclass IS-A specialized version of parent")
    print("  • Example: Manager IS-A Employee")
    print("\nComposition (HAS-A):")
    print("  • Object HAS-A component")
    print("  • Example: Person HAS-A Address")
    print("  • More flexible, prefer composition over inheritance")
    print("="*70)


if __name__ == "__main__":
    main()