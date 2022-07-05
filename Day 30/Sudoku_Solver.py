# Python | Day 30
# Sudoku Solver.
# TASK: We'd be coding a SUDOKU SOLVER today!
# Write a function that takes in a 9x9 array of NUMBERS.
# Let this list represent a partially filled grid of numbers(specifically,
# of integers ranging from 1 to 9, where "0" signifies an empty space in the grid.)
# as parameters, and returns as a 9x9 array, the solution(s) to it. If there are no solutions, return False.
# Exceptions:
# *If an empty list or an invalid list(list with numbers outside the 1-9 range,
# or empty lists, or a list of wrong size, etc.) is input, it issues a warning.
# (Hint: Backtracking is one effective method for solving this problem-it is however, not the only method.)

def get_array():
    """A function to get the user's Sudoku."""
    try:
        print("Please enter your array row-wise. Enter 0 for empty cells: ")

        user_sudoku = []
        for i in range(9):
            row_nums = []
            for j in range(9):
                num = int(input("Enter: "))
                row_nums.append(num)
            user_sudoku.append(row_nums)

        return user_sudoku
    except ValueError:
        print("Please enter ONLY integer values.")


def check(array, row, col, num):
    """A function to iterate through the array and check if a number exists twice in a given row,
    column or in the same smaller 3*3 matrix.
    """

    # This checks if we can find the same number in the same row, it returns False if we do.
    for i in range(9):
        if array[row][i] == num:
            return False

    # This checks if we can find the same number in the same column, it returns False if we do.
    for j in range(9):
        if array[j][col] == num:
            return False

    # This checks if we can find the same number in the same 3*3 matrix, it returns False if we do.
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if array[i + start_row][j + start_col] == num:
                return False
    return True


def sudokusolver(array, row, col):
    """A function that solves a sudoku game."""

    try:
        N = 9
        # checks if we have reached the last row and column respectively and returns True.
        if row == N - 1 and col == N:
            return True

        # Check if we are in the 9th column, moves to the next row and column again starts from zero.
        if col == N:
            row += 1
            col = 0

        # Check if the current position of the array contains a value > 0, we iterate for next column
        if array[row][col] > 0:
            return sudokusolver(array, row, col + 1)

        for num in range(1, N + 1, 1):

            # checks if we can place the num(1-9) in the given position then moves to the next column.
            if check(array, row, col, num):

                # Assigns the num in the current position of the array
                # and assumes our assigned num in the position is correct.
                array[row][col] = num

                # Checks for next possibility with next column
                if sudokusolver(array, row, col + 1):
                    return True

            # Removes the assigned number and goes for the next assumption.
            array[row][col] = 0
        return False
    except TypeError:
        print("Please enter numbers 1-9 only and enter 0 for empty cells.")


def print_solution():
    """A function to print the Sudoku solution."""

    user_sudoku = get_array()
    if sudokusolver(user_sudoku, 0, 0):
        print("Here is your sudoku solution:")
        for i in range(9):
            for j in range(9):
                print(user_sudoku[i][j], end=" ")
            print()
    else:
        print(False)


print_solution()
