def safe_divide(numerator, denominator):
    try:
        numerator = float(input("enter the numerator: "))
        denominator = float(input("enter the denominator: "))

        #return float(numerator)/float(denominator)
        return(f"The result of the division is {float(numerator)/float(denominator):.1f}")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."