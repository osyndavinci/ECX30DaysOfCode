# python | Day 24
# Bubble sort.
# "Bubble sort" is a basic algorithm for sorting (rearranging in ascending or descending order) elements in a list.
# It operates as follows: 1) Iterate across a list, element by element.
# 2) Upon encountering any two adjacent elements which are in the "wrong" designated order(ascending or descending),
# swap their positions in the list-else, do nothing!
# 3) Do this until your iteration reaches the end of the list.
# 4) Repeat steps 1) through 3) until there are no longer any adjacent elements in the "wrong" order. Then STOP.
# (See more at: Bubble sort.)
# Write a function that takes in two parameters, one list of alphabets,
# and one flag designating what order in which to sort. Using the Bubble sort algorithm,
# have this function return a SORTED version of the input list.
# E.G: f(['x', 'c', 'b', 'v', 'z', 'a'], "descending") => ['a', 'b', 'c', 'v', 'x', 'z']
# Note: Type checking(or Exception Handling) is necessary. Disregard case-sensitivity.


def bubble_sort(arr, order):
    """A function to sort an array(list) of items in a particular order."""

    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j + 1]) and (order.lower() == "ascending"):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif (arr[j] < arr[j + 1]) and (order.lower() == "descending"):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


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
    length = getint("How many items are in your list? Please enter the number her: ")
    user_list = [(input("enter: ")) for i in range(length)]
    list_order = str(input("Please enter the order in which it should be sorted."
                           "(eg. 'ascending' or 'descending'): "))

    print(f"The sorted array in {list_order} order is: ", bubble_sort(user_list, list_order))

            
taskmanager()
