"""
Topic: Re-raising Exceptions.

Sometimes you want to log an error or perform some cleanup 
but still let the exception propagate up to the caller. 
Use a bare 'raise' to re-raise the active exception while 
preserving the original traceback.
"""

def log_and_re_raise():
    try:
        # Imagine a database failure
        raise ConnectionError("DB Timeout")
    except ConnectionError:
        print("[Log] Database connection failed. Logging event...")
        # Re-raise the exact same exception
        raise 

if __name__ == "__main__":
    try:
        log_and_re_raise()
    except ConnectionError as e:
        print(f"Main App caught re-raised error: {e}")
