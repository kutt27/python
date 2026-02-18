"""
Transaction Risk logic.
"""

def categorize_transaction(
    amount: float,
    is_international: bool,
    is_high_risk_merchant: bool,
    customer_category: str
) -> str:
    """
    Categorizes transaction for fraud detection.
    
    Args:
        amount: Transaction amount
        is_international: Whether transaction is international
        is_high_risk_merchant: Whether merchant is flagged as high-risk
        customer_category: Customer category (new/regular/vip)
    
    Returns:
        Risk category: "low", "medium", or "high"
    
    Real-world use case: Fraud detection, payment processing.
    """
    # High risk conditions
    if is_high_risk_merchant or (is_international and amount > 5000):
        return "high"
    
    # Medium risk conditions
    if (amount > 1000 and customer_category == "new") or is_international:
        return "medium"
    
    # VIP customers get lower risk scoring
    if customer_category == "vip":
        return "low"
    
    # Default based on amount
    return "medium" if amount > 500 else "low"


def demonstrate_risk_analysis() -> None:
    """
    Demonstrates fraud risk categorization using logical AND/OR.
    
    Real-world use case: Payment processing.
    """
    transactions = [
        (100, False, False, "regular", "Small local purchase"),
        (2000, False, False, "new", "Large purchase, new customer"),
        (500, True, False, "vip", "International, VIP customer"),
        (1000, False, True, "regular", "High-risk merchant"),
        (6000, True, False, "regular", "Large international"),
    ]
    
    for amount, intl, high_risk, cust_cat, description in transactions:
        risk = categorize_transaction(amount, intl, high_risk, cust_cat)
        risk_icons = {"low": "🟢", "medium": "🟡", "high": "🔴"}
        
        print(f"{risk_icons[risk]} {risk.upper():6} | ${amount:>7.2f} | {description}")


if __name__ == "__main__":
    demonstrate_risk_analysis()
