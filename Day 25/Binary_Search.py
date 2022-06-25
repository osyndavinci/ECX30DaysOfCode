# python | Day 25
# Binary search algorithm.
# "Binary search" is a basic algorithm, used to find the position of a target value within an SORTED LIST.
# (More details can be found here: Binary search).
# For today's task, write a function that takes in two parameters: One list of alphabets,
# and one character to search. E.G f("x", ['m', 'v', 'x', 'u']) In your function:
# 1)first check if the input list is sorted, using any method of your preference.
# (If it's unsorted, return a warning indicating so, else continue)
# 2) Using the BINARY SEARCH ALGORITHM, find the position of the input character in the sorted list.
# 3)return the position of the character in the search list.
# 4) If the character is not found, return false.


def binarysearch(char, userlist):
    """A function to find the position of target value within a sorted list."""

    if userlist != sorted(userlist):
        return "Error! Please sort your list."
    else:
        n = len(userlist)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if userlist[mid] == char:
                pos = mid + 1                   # added a one because counting starts from zero in computing.
                return pos
            elif userlist[mid] < char:
                start = mid + 1
            else:
                end = mid - 1
        return False


def taskmanager():
    """A function to manage and call the above function."""

    user_list = list(input("Please enter your list of alphabets in this way(eg. abcdefghi): "))
    target = str(input("Enter your target character: "))
    output = binarysearch(target, user_list)
    print(output)


taskmanager()
