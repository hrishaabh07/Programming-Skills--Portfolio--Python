# Loop 1: Count upwards from 0 to 50 by steps of 1
print("Counting up from 0 to 50:")
for num in range(0, 51):  # Loop starts at 0 and ends at 50
    print(num)

# Loop 2: Count downwards from 50 to 0 by steps of 1
print("\nCounting down from 50 to 0:")
for num in range(50, -1, -1):  # Loop starts at 50 and ends at 0
    print(num)

# Loop 3: Count upwards from 30 to 50 by steps of 1
print("\nCounting up from 30 to 50:")
for value in range(30, 51):  # Loop starts at 30 and ends at 50
    print(value)

# Loop 4: Count downwards from 50 to 10 by steps of 2
print("\nCounting down from 50 to 10 by twos:")
for value in range(50, 9, -2):  # Loop starts at 50 and stops just before 10
    print(value)

# Loop 5: Count upwards from 100 to 200 by steps of 5
print("\nCounting up from 100 to 200 by fives:")
for counter in range(100, 201, 5):  # Loop starts at 100 and ends at 200
    print(counter)