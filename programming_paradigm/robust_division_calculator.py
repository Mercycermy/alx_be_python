def safe_divide(numerator, denominator):
    """Performs division with error handling for division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float for division
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
