# python | Day 5
# Fibonacci
# Using recursion, write a function that prints out the first "n" members of the Fibonacci series.
# The Fibonacci series is a series of integers, starting from 0 and 1,
# for which each term is the sum of the two preceding terms. i.e [0,1,1,2,3,5,8,13,21,...];
# OR "fib(n+1) = fib(n) + fib(n-1)"

x = int(input("Please enter the number of terms of your Fibonacci series: "))
# gets the number of the terms in the fibonacci series from the user


def fib(n):
    """ A function to calculate fibonacci series using recursion.
    The function return 0 and 1 when n is 0 and 1.
    To calculate fib(n), the function first calculates fib(n-2), then fib(n-1) using
    fib(n-2) then adds them together to get fib(n).

    This though, is not very efficient when n gets above 30 because the function has to
    call itself twice to calculate the large values.

    """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


for i in range(x):               # This for loop prints the series to the range entered by the user.
    print(fib(i), end=" ")
