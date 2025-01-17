# Defining the  global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

# Function  that handles the convertion of Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    #Converting Fahrenheit to Celsius.
    return (fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR) -32
 
# Function that handles the convertion Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    #Converting Celsius to Fahrenheit.
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temp_input = float(input("Enter the temperature to convert: "))
        #temperature = float(temp_input)  # Convert to float

        # Prompt user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted_temp = convert_to_celsius(temp_input)
            print(f"{temp_input:.1f}\u00b0F is {converted_temp:.2f}\u00b0C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temp_input)
            print(f"{temp_input:.1f}\u00b0C is {converted_temp:.2f}\u00b0F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
