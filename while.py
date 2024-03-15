# sum of numbers entered by user is stored in the variable below
num_total = 0

# variable to count input numbers
count = 0

# Continually ask the user to enter a number
while True:
    number = int(input("Enter a number (enter -1 to stop): "))

    # Check if the user wants to stop
    if number == -1:
        break
    # Update num_total and count
    num_total += number
    count += 1

# Calculate the average
if count > 0:
    # average is defined, it is calculated by dividing the total of numbers by count
    average = num_total / count
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers entered.")
