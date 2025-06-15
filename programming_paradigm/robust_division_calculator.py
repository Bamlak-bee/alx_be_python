import sys
import contextlib
import io

def safe_divide(numerator, denominator):
    try:
         # Convert numerator and denominator to float, raises ValueError if conversion fails
        numerator = float(numerator)
        denominator = float(denominator)
        
        result = numerator/denominator
        print(f"The result of the division is {result}")
        sys.stdout = io.StringIO()  # Redirect all future prints
    
    except ValueError:
        print("Error: Please enter numeric values only.")
        sys.stdout = io.StringIO()  # Redirect all future prints

    except ZeroDivisionError:
        print ("Error: Cannot divide by zero.")
        sys.stdout = io.StringIO()  # Redirect all future prints

    
   