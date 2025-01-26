from datetime import datetime, timedelta

def display_current_datetime():
    #Displaying the current date and time in the format YYYY-MM-DD HH:MM:SS.
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    #Calculating and displaying future date based on user input
    try:
        Days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=Days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
  
   

