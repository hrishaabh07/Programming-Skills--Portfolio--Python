# Collect user inputs for personal details: full name and place of origin
full_name = input("Enter your full name: ")
place_of_origin = input("Enter your place of origin: ")

# Ensure the provided age is a valid numerical value
while True:
    age_entry = input("Enter your age: ")
    if age_entry.isdigit():  # Confirm that the age input is numeric
        user_age = int(age_entry)  # Convert the validated input to an integer
        break
    else:
        print("Invalid input. Please provide a numerical age.")

# Organize the collected details into a dictionary
user_details = {
    "full_name": full_name,
    "place_of_origin": place_of_origin,
    "user_age": user_age
}

# Present the stored details back to the user
print(f"Name: {user_details['full_name']}")
print(f"Hometown: {user_details['place_of_origin']}")
print(f"Age: {user_details['user_age']}")