def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        print(f"The result of the division is {result}")
    except Exception as e:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
    else:
        raise ValueError("Error: Please enter numeric values only.")