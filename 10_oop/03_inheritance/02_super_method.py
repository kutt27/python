"""
Topic: Using `super()`.

`super()` allows a child class to call methods from its parent class, 
common for extending `__init__` while keeping parent logic.
"""

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        # Call parent's __init__ to handle name and salary
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return f"Manager: {self.name}, Dept: {self.department}, Salary: ${self.salary}"

if __name__ == "__main__":
    mgr = Manager("Alice", 90000, "Engineering")
    print(mgr.get_info())
