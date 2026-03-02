"""
Topic: Method Overriding.

A child class can provide a specific implementation of a method 
that is already defined in its parent class.
"""

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        """Override parent method with specific sound."""
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow...")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Animal()]
    
    for animal in animals:
        # Polymorphism in action: same method name, different behavior
        animal.make_sound()
