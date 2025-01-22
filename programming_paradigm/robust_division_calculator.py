def safe_divide(numerator, denominator):
    try:
        numerator = float(input("enter the numerator: "))
        denominator = float(input("enter the denominator: "))

        return numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except ValueError:
        print("Error: Please enter numeric values only")