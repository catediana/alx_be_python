def main():
    # Prompt the user to enter a positive integer
    size = int(input("Enter the size of the pattern: "))
    
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Use a while loop to iterate through rows
    row = 0
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after printing a row
        row += 1

if __name__ == "__main__":
    main()
