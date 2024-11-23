# Set the predefined correct password
correct_code = "12345"

# Define the maximum number of allowed attempts
max_attempts = 5

# Initialize the counter for the number of attempts used
attempt_count = 0

# Keep prompting the user for the password until the correct one is entered or attempts are exhausted
while attempt_count < max_attempts:
    # Ask the user to input the password
    entered_code = input("Enter the password: ")
    
    # Check if the entered password matches the predefined one
    if entered_code == correct_code:
        print("Access granted. Welcome!")
        break
    else:
        # Increment the number of failed attempts
        attempt_count += 1
        # Calculate and display the remaining attempts
        remaining_attempts = max_attempts - attempt_count
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Too many failed attempts. Authorities have been notified.")
            