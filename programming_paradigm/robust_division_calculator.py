def safe_divide(numerator, denominator):
    """Performs division and handles errors gracefully."""
    try:
        # Convert inputs to floats and perform division
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Division by zero is not allowed."

        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Both numerator and denominator must be valid numbers."
