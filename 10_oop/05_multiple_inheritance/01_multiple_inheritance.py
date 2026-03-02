"""
Topic: Multiple Inheritance.

In Python, a class can inherit from more than one parent class.
"""

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class Authenticator:
    def authenticate(self, user):
        print(f"Authenticating user '{user}'...")
        return True

class AdminInterface(Logger, Authenticator):
    """Inherits features from both parents."""
    def run(self, user):
        if self.authenticate(user):
            self.log("Admin interface accessed.")

if __name__ == "__main__":
    admin = AdminInterface()
    admin.run("alice_admin")
