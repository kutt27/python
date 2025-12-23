"""
Functional Python: Monads (Result Pattern)
===========================================

Topic: Handling execution flow without exceptions using Result/Maybe

Concept:
Instead of raising exceptions, functions return a wrapper object:
- Success(value)
- Failure(error)
This allows chaining operations safely.
"""

from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, Union

T = TypeVar('T')
E = TypeVar('E')
U = TypeVar('U')

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T
    
    def bind(self, func: Callable[[T], 'Result']) -> 'Result':
        return func(self.value)

@dataclass(frozen=True)
class Failure(Generic[E]):
    error: E
    
    def bind(self, func) -> 'Result':
        return self # Skip future steps, propagate error

# Union Type for Result
Result = Union[Success[T], Failure[str]]


# --- Business Logic Steps ---

def parse_input(data: str) -> Result[int]:
    if data.isdigit():
        return Success(int(data))
    return Failure(f"Invalid number: '{data}'")

def validate_age(age: int) -> Result[int]:
    if age >= 18:
        return Success(age)
    return Failure("Too young")

def grant_access(age: int) -> Result[str]:
    return Success(f"Access Granted to age {age}")


def workflow(input_data: str) -> Result[str]:
    """Chaining using the 'bind' concept."""
    # This is effectively: parse -> bind(validate) -> bind(grant)
    return (
        parse_input(input_data)
        .bind(lambda x: validate_age(x))
        .bind(lambda x: grant_access(x))
    )

def main():
    print("="*70)
    print("MONAD PATTERN (Railway Oriented Programming)".center(70))
    print("="*70)
    
    test_cases = ["25", "10", "abc"]
    
    for case in test_cases:
        print(f"\nProcessing '{case}':")
        result = workflow(case)
        
        if isinstance(result, Success):
            print(f"  🟢 Success: {result.value}")
        else:
            print(f"  🔴 Failure: {result.error}")
            
            
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Monads wrap values and control sequencing")
    print("• 'bind' (or flat_map) unwrap value and apply next function")
    print("• If any step fails, the whole chain fails gracefully")
    print("• No try-except blocks needed in the business logic flow")
    print("="*70)


if __name__ == "__main__":
    main()
