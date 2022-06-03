# python | Day 3
# Palindromic numbers
# A palindrome is a word that reads the same way forwards and backwards.(E.g Tenet, 101101)
# Write a function that prints out all Palindromic numbers less than a given input,
# and returns the total number —of palindromes— found!
# E.G: f(500) would print all Palindromic numbers less than 500,
# as well as the total number of palindromes less than 500.

num_range = int(input("Please enter the limit of your palindrome numbers: "))
# getting the input range from the user


def palin_func(n: int) -> bool:
    """ A Boolean function to test for palindromes.

    rev(int): this variable is used to find the reverse of n.
    digit(int): this variable returns the modulus of n using the modulus operator(%).
    num(int): this variable is assigned the value of n.

    """
    rev = 0
    num = n
    while num > 0:                 # ensures that the input range is greater than zero(0)
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    return n == rev                # returns the boolean expressions(True or False) for a given value of n.


x = 0                              # initializing the palindrome counter.
for i in range(10, num_range):     # iterates over the range giving by the user starting from 10.
    if palin_func(i):              # if palin_func(i) is not False
        x += 1                     # increases by 1 for any palindrome found during the iteration
        print(i, end=" ")          # prints all the palindromes separating them by a space

print("\nThere are {} palindromes in this range.".format(x))  # prints the number of palindromes in the given range

palin_numbers = palin_func(num_range)   # calls the palindrome function with argument of num_range
