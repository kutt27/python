"""
Topic: Mixins Pattern.

Mixins are small, specialized classes used to add specific behavior 
to other classes via multiple inheritance. They aren't meant 
to be used on their own.
"""

class JsonMixin:
    """Adds a 'to_json' method to any class."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class TimestampMixin:
    """Adds a 'ts' attribute to any class."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.ts = datetime.now().isoformat()

class Task(TimestampMixin, JsonMixin):
    def __init__(self, title):
        # super() handles the MRO chain including Mixins
        super().__init__()
        self.title = title

if __name__ == "__main__":
    t = Task("Buy Milk")
    print(f"Task TS: {t.ts}")
    print(f"JSON:    {t.to_json()}")
