# Function to determine if a number is even or odd
def check_parity(number):
    # Check the parity of the number
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Function to handle program execution
def start_program():
    # Get a number from the user
    user_input = int(input("Enter a number: "))
    # Check its parity and get the result
    result_message = check_parity(user_input)
    # Output the result
    print(result_message)

# Run the program only when executed directly
if __name__ == "__main__":
    start_program()
