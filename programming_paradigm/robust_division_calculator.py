def safe_divide(numerator, denominator):
    """
    Perform division while handling errors like division by zero and non-numeric inputs.

    Args:
        numerator: The numerator as a string.
        denominator: The denominator as a string.

    Returns:
        A string with the result or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        # Format result without unnecessary trailing zeros
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."
