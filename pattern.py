# the variable for row count (n) is named
star_pattern_rows = 9

# the variable for stars is named
stars = "*"

# a for loop that iterates over the range from 1 to 10 to give 9 iterations is created
# i represent each row number

for i in range(1, 10):

    # if row number is less or equal to 5, the number of stars will increase over each iteration by 1
    if i <= 5:
        print(stars * i)

    # the following command (10 - i) reduces the number of stars to print out by 1 once i exceeds 5
    else:
        print(stars * (10 - i))
