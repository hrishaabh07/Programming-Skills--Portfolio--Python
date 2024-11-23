# Define a mapping of month numbers to their corresponding days
month_days = {
    1: 31,  # January
    2: 28,  # February (default, adjusted later for leap years)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Prompt the user to enter a month number
month_input = input("Enter the month number (1-12): ")

# Check if the input is valid
if month_input.isdigit():
    month_num = int(month_input)  # Convert input to an integer
    if 1 <= month_num <= 12:
        # Adjust for leap years if the month is February
        if month_num == 2:
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            if is_leap == "yes":
                print("This month has 29 days.")
            else:
                print("This month has 28 days.")
        else:
            # Print the number of days for other months
            print(f"This month has {month_days[month_num]} days.")
    else:
        # Handle invalid month numbers
        print("Error: Please enter a valid month number between 1 and 12.")
else:
    # Handle non-numeric inputs
    print("Error: Please enter a numeric month number.")