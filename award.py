# users will input the time taken to complete their swimming, cycling and runnig activities
swimming_time = int(input("How many minutes did you spend swimming?"))
cycling_time = int(input("How many minutes did you spend cycling?"))
running_time = int(input("How many minutes did you spend running?"))

# the three activities are reffered to as triathlon
sum_triathlon = int((swimming_time + cycling_time + running_time))

# total taken to complete the three activities will be calculated
print(sum_triathlon)

# the if statement is a command statement that determines whether or not the indented statement will be executed. 
#if the condition is True, the indented statement will print
if sum_triathlon <= 100:
    print("You will receive provincial colours")

# the elif statement allows us to specify a new condition
elif (sum_triathlon == 101) and (sum_triathlon <= 105):
    print("You will receive provincial half colours")

# another condition is tested
elif (sum_triathlon == 106) and (sum_triathlon <= 110):
    print("You will receive provincial scroll")

# the else statement we run if all the if and elif statement above are False
else:
    print("No award!")
