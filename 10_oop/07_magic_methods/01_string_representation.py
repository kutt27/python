"""
Topic: String Representations (`__str__` and `__repr__`).

`__str__`: User-friendly informal string for display (print, format).
`__repr__`: Official/technical unambiguous string for developers.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
        
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

if __name__ == "__main__":
    b = Book("1984", "George Orwell")
    
    # print() uses __str__
    print(f"Main output: {b}")
    
    # Debugging/Shell uses __repr__
    print(f"Debug string: {repr(b)}")
