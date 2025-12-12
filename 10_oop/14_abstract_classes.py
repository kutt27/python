"""
Python OOP: Abstract Base Classes (ABC)
========================================

Topic: Abstract classes, interfaces, enforcing contracts

Real-World Applications:
- Framework design
- Plugin systems
- Interface definitions
- Enforcing API contracts
"""

from abc import ABC, abstractmethod
from typing import List


class DataProcessor(ABC):
    """Abstract base class for data processors."""
    
    @abstractmethod
    def process(self, data: str) -> str:
        """Process data (must be implemented by subclasses)."""
        pass
    
    @abstractmethod
    def validate(self, data: str) -> bool:
        """Validate data (must be implemented)."""
        pass
    
    def log(self, message: str):
        """Concrete method (optional to override)."""
        print(f"[LOG] {message}")


class JSONProcessor(DataProcessor):
    """JSON data processor implementation."""
    
    def process(self, data: str) -> str:
        """Process JSON data."""
        self.log("Processing JSON")
        return f"Processed: {data}"
    
    def validate(self, data: str) -> bool:
        """Validate JSON format."""
        return data.startswith("{") and data.endswith("}")


class XMLProcessor(DataProcessor):
    """XML data processor implementation."""
    
    def process(self, data: str) -> str:
        """Process XML data."""
        self.log("Processing XML")
        return f"<processed>{data}</processed>"
    
    def validate(self, data: str) -> bool:
        """Validate XML format."""
        return data.startswith("<") and data.endswith(">")


class StorageBackend(ABC):
    """Abstract storage interface."""
    
    @abstractmethod
    def save(self, key: str, value: str) -> bool:
        """Save data."""
        pass
    
    @abstractmethod
    def load(self, key: str) -> str:
        """Load data."""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete data."""
        pass


class FileStorage(StorageBackend):
    """File-based storage implementation."""
    
    def __init__(self):
        self.data = {}  # Simulating file storage
    
    def save(self, key: str, value: str) -> bool:
        self.data[key] = value
        print(f"Saved to file: {key}")
        return True
    
    def load(self, key: str) -> str:
        return self.data.get(key, "")
    
    def delete(self, key: str) -> bool:
        if key in self.data:
            del self.data[key]
            print(f"Deleted from file: {key}")
            return True
        return False


class DatabaseStorage(StorageBackend):
    """Database storage implementation."""
    
    def __init__(self):
        self.data = {}  # Simulating database
    
    def save(self, key: str, value: str) -> bool:
        self.data[key] = value
        print(f"Saved to database: {key}")
        return True
    
    def load(self, key: str) -> str:
        return self.data.get(key, "")
    
    def delete(self, key: str) -> bool:
        if key in self.data:
            del self.data[key]
            print(f"Deleted from database: {key}")
            return True
        return False


def process_with_any_processor(processor: DataProcessor, data: str):
    """Function accepting any DataProcessor implementation."""
    if processor.validate(data):
        result = processor.process(data)
        print(f"Result: {result}")
    else:
        print("Invalid data format")


def main():
    """Demonstrates abstract base classes."""
    print("="*70)
    print("ABSTRACT BASE CLASSES (ABC)".center(70))
    print("="*70)
    
    print("\n[1] CANNOT INSTANTIATE ABSTRACT CLASS")
    print("-" * 70)
    
    try:
        processor = DataProcessor()  # Error!
    except TypeError as e:
        print(f"✗ Error: {e}")
    
    print("\n[2] CONCRETE IMPLEMENTATIONS")
    print("-" * 70)
    
    json_proc = JSONProcessor()
    xml_proc = XMLProcessor()
    
    json_data = '{"key": "value"}'
    xml_data = '<data>value</data>'
    
    print("JSON Processor:")
    process_with_any_processor(json_proc, json_data)
    
    print("\nXML Processor:")
    process_with_any_processor(xml_proc, xml_data)
    
    print("\n[3] POLYMORPHISM WITH ABC")
    print("-" * 70)
    
    processors: List[DataProcessor] = [json_proc, xml_proc]
    
    print("Processing with different implementations:")
    for proc in processors:
        print(f"  Using {type(proc).__name__}")
        proc.log("Starting processing")
    
    print("\n[4] STORAGE BACKEND ABSTRACTION")
    print("-" * 70)
    
    # Can swap implementations easily
    storage: StorageBackend = FileStorage()
    storage.save("user:1", "Alice")
    print(f"Loaded: {storage.load('user:1')}")
    
    # Switch to different backend
    storage = DatabaseStorage()
    storage.save("user:1", "Bob")
    print(f"Loaded: {storage.load('user:1')}")
    
    print("\n" + "="*70)
    print("ABC Benefits:")
    print("-" * 70)
    print("✓ Enforce method implementation in subclasses")
    print("✓ Define clear interfaces/contracts")
    print("✓ Enable polymorphism")
    print("✓ Catch missing implementations at instantiation")
    print("\nUse Cases:")
    print("  • Plugin systems")
    print("  • Strategy pattern")
    print("  • Framework design")
    print("  • Swappable backends")
    print("="*70)


if __name__ == "__main__":
    main()
