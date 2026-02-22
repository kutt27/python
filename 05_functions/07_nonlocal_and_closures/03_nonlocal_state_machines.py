"""
Topic: Nonlocal State Machines.

A simple state machine implemented using closures and `nonlocal` 
to track transitions.
"""

def create_order_tracker():
    """Hides state behind a functional interface."""
    state = "pending"
    
    def transition(new_state: str):
        nonlocal state
        valid_moves = {
            "pending": ["shipped", "cancelled"],
            "shipped": ["delivered"],
            "delivered": []
        }
        
        if new_state in valid_moves.get(state, []):
            print(f"Status: {state} → {new_state}")
            state = new_state
            return True
        
        print(f"Error: Cannot move from {state} to {new_state}")
        return False

    return transition

if __name__ == "__main__":
    tracker = create_order_tracker()
    tracker("shipped")
    tracker("cancelled") # Invalid
    tracker("delivered")
