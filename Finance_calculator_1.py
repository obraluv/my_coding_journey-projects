import math
# purpose of investment and bond will be output
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond- to calculate the amount you will have to pay on a home loan\n")

# this line of code will ask the user to choose what they what to calculate
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# the operator or is used to ensure  that if the user inputs 'investment in any
# of the below format, the program will not be affected
# if statement is used to ensure the program runs if the condition above is True
if user_choice == "Investment".lower():
    
    # a while loop in conjuction with a try-except block is implemented to ensure that incase a user's
    # input is incorrect, instead of the program breaking,the loop will continue with an output of what 
    #is expected of the user until the correct entry is input.
    while True:
        try:
            p = float(input("Enter the amount you're depositing:a numeric value greater than zero:"))
            if p > 0:
                break
            else:
                print("Please enter a value greater than 0")
        except ValueError:
            print("Invalid input, please enter a numeric value")

    i = float(input("Enter the interest rate:"))
    t = float(input("Enter the number of year you're investing:"))

    # the command below ask the user to input what kind of interest is applicable to them
    interest = input("Enter interest type.(Simple_interest / Compound_interest): ")

    r = i / 100  # divide the interest rate by 100

    # another if statement is nested inside the first if-statement above,
    # this condition will only be checked if the first if-condition is True
    # if user input investment from above, the below code will run
    if interest == "Simple_interest".lower():
        
        # the formula below will calculate the total amount to be paid after simple interest is applied
        Amount = p * (1 + r * t)
    
    # this condition will only be checked if the second if condition above is False
    # if user input investment from above, the below code will run
    elif interest == "Compound_interest".lower():
    
    # the below formula will be used to get total amount to be paid
        Amount = p * math.pow((1 + r), t)
    print(f"total amount after interest is applied is {Amount:.2f}")

# if the first if-statement above is False, that is the user input 'bond' and not 'investment
# the following code will run
# the operator or is used to ensure  that if the user inputs 'bond' in any
# of the below format, the program will not be affected
elif user_choice == "Bond".lower():
    while True:
        try:
            p = float(input("Enter the present value of the house:a numeric value greater than zero:"))
            if p > 0:
                break
            else:
                print("Please enter a value greater than 0")
        except ValueError:
            print("Invalid input, please enter a numeric value")

    r = float(input("Enter the rate of interest: "))
    n = float(input("Enter the number of months for the bond: "))

    i = r / 100 / 12  # divide the interest rate by 100 and then by 12

# since monthly interest rate (i) is calculated by dividing annual interest rate by 12
    repayment = (i * p) / (1 - (1 + i) ** (-n))
    

    print(f"The repayment after {n} months is {repayment:.2f}")

# the else condition will run if all the statement above are False
else:

    print("No repayment!")

