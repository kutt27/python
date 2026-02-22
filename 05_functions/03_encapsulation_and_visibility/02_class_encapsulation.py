"""
Topic: Encapsulation with Classes and Methods.

Hiding complexity behind a clean public interface. Callers 
don't need to know how payments are processed, just that they are.
"""

class PaymentProcessor:
    def _validate_card(self, card: str) -> bool:
        """Private method for internal validation."""
        print(f"  Validating {card[-4:]}...")
        return len(card) == 16

    def _charge(self, amount: float):
        """Private method for actual charging logic."""
        print(f"  Charging ${amount}...")
        return "TXN-OK-123"

    def process(self, card_number: str, amount: float):
        """Public interface for the payment system."""
        if not self._validate_card(card_number):
            return {"success": False, "error": "Invalid card"}
        
        tx_id = self._charge(amount)
        return {"success": True, "transaction_id": tx_id}

if __name__ == "__main__":
    proc = PaymentProcessor()
    result = proc.process("1234567812345678", 99.99)
    print(f"Result: {result}")
