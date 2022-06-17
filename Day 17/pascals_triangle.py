# python | Day 17
# Pascal's Triangle.
# An easy one. Write a function that prints out thr first "n" rows of Pascal's Triangle
# -Where "n" is an integer taken as an argument of the function.

def pascal_solver(num):
    """ A function that prints out the first "n" rows of a Pascal's Triangle."""

    for i in range(1, num+1):
        for j in range(0, num-i+1):
            print(' ', end='')

        c = 1                       # 1 is always the first element
        for j in range(1, i+1):
            print(' ', c, sep='', end='')       # 1 is always starts each row.

            c = c * (i - j) // j            # using Binomial coefficient

        print()


def getint(prompt):
    """ A function to get an integer input from the user.
    it also handles the errors/exception that the user might encounter.
    """

    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")


def taskmanager():
    """ This function runs the program by calling the functions above."""

    user_num = getint("Please enter the number of rows: ")
    pascal_solver(user_num)


taskmanager()
