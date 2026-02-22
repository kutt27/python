"""
Topic: Factory Functions.

Using closures to create specialized functions. This is 
useful for creating pre-configured loggers, multipliers, 
or validators.
"""

def make_logger(service_name: str):
    """Factory that creates loggers with specific context."""
    log_count = 0
    
    def log(message: str):
        nonlocal log_count
        log_count += 1
        print(f"[{service_name}] (#{log_count}) {message}")
        
    return log

if __name__ == "__main__":
    api_logger = make_logger("API")
    db_logger = make_logger("Database")
    
    api_logger("Server started")
    db_logger("Connected to PostgreSQL")
    api_logger("Processing request")
