"""
Eligibility Evaluation logic.
"""

def evaluate_eligibility(
    age: int,
    has_license: bool,
    credit_score: int,
    employment_status: str
) -> tuple[bool, str]:
    """
    Evaluates eligibility for a service (e.g., car rental).
    
    Args:
        age: Applicant's age
        has_license: Whether applicant has valid license
        credit_score: Credit score (300-850)
        employment_status: Employment status
    
    Returns:
        Tuple of (is_eligible, reason)
    
    Real-world use case: Loan approval, service eligibility, risk assessment.
    """
    # Must meet basic requirements
    if age < 21:
        return (False, "Must be 21 or older")
    
    if not has_license:
        return (False, "Valid license required")
    
    # Credit and employment checks
    if credit_score < 600 and employment_status != "employed":
        return (False, "Insufficient credit score and not employed")
    
    # Either good credit OR employed can qualify
    if credit_score >= 650 or (credit_score >= 600 and employment_status == "employed"):
        return (True, "Eligible")
    
    return (False, "Does not meet credit/employment requirements")


def demonstrate_eligibility() -> None:
    """
    Demonstrates eligibility evaluation using multiple criteria.
    
    Real-world use case: Loan/Service approval systems.
    """
    applicants = [
        (25, True, 700, "employed", "Good applicant"),
        (19, True, 750, "employed", "Too young"),
        (25, False, 750, "employed", "No license"),
        (25, True, 650, "unemployed", "Good credit"),
        (25, True, 550, "unemployed", "Low credit + not employed"),
    ]
    
    for age, license, credit, employment, description in applicants:
        eligible, reason = evaluate_eligibility(age, license, credit, employment)
        status = "✓ ELIGIBLE" if eligible else "✗ DENIED"
        print(f"{status:12} | {description:25} | {reason}")


if __name__ == "__main__":
    demonstrate_eligibility()
