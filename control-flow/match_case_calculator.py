def main():
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        case _:
            print("Invalid operation. Please choose one of (+, -, *, /).")
            return

    # Display the result
    print(f"The result is {result}.")

if __name__ == "__main__":
    main()
