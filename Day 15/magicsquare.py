# python | Day 15
# A Magic Square is a 3*3 grid, such that: It contains ALL the numbers 1 through 9 The sum of each row,
# each column, and each diagonal all add up to the same number.
# In a program, you can simulate a magic square using a two-dimensional list.
# *Write a function that accepts a two-dimensional list as input,
# and determines whether the list is a Magic Square or not. Test the function in a program.


def checksquare(user_list):
    """ A function to check if a square matrix is a Magic Square."""

    x = len(user_list)

    diag1_sum = 0   # initializes the leading diagonal summation to zero.
    diag2_sum = 0   # initializes the counter-diagonal summation to zero.

    for i in range(x):
        diag1_sum += user_list[i][i]           # (i,i) is the position of  each diag1_sum value, eg.(0,0), (1,1)...
        diag2_sum += user_list[i][x-i-1]       # (i, x-i-1) is the position of each diag2_sum value, eg.(0,2), (1,1)...

    if not (diag1_sum == diag2_sum):            # if the two diagonals are not equal, then it is not a magic square.
        return False
    for i in range(x):
        row_sum = 0                                     # row_sum is the sum of the row values initialized at 0.
        col_sum = 0                                     # col_sum is the sum of the column values initialized at 0.
        for j in range(x):
            row_sum += user_list[i][j]
            col_sum += user_list[j][i]
        if not (row_sum == col_sum == diag1_sum):       # if the sums are not equal then it is not a magic square.
            return False
    return True                                         # if all the conditions are met then it is a magic square.


print("Please enter a 2D 3*3 List/Matrix row-wise.")
mat_list = [[int(input("enter: ")) for n in range(3)] for m in range(3)]
# A list comprehension that allows the user to enter nine(9) integer values and converts it to a 2D 3*3 list.


if checksquare(mat_list):
    print(f"The matrix {mat_list} is a Magic Square.")
else:
    print(f"The Matrix {mat_list} is not a Magic Square.")
