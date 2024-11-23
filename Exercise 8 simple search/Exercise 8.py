# Initialize a list of names to search from
name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a name to search for
search_name = input("Enter the name you want to search for: ")

# Check if the entered name is in the list
if search_name in name_list:
    print(f"{search_name} was found in the list!")
else:
    print(f"Sorry, {search_name} is not in the list.")