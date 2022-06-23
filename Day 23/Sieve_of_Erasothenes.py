# python | Day 23
# Sieve of Erasothenes.
# The sieve of erasothenes is an ancient algorithm for finding all primes less than a given value N.
# It operates as follows:
# 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
# 2. Initially, let p equal 2, the smallest prime number.
# 3. Enumerate the multiples of p by
# counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...;
# the p itself should not be marked).
# 4. Find the smallest number in the list greater than p that is not marked.
# If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime),
# and repeat from step 3.
# 5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
# 6. (See more: Sieve of Erasothenes).
# Using the Sieve of Erasothenes (as described above),
# Write a function that takes in an integer as input, and returns a list containing all primes
# less than that input number.


def sieve_of_erasothenes(n):
    """ A function to return all prime numbers up to a given input number."""

    prime = [True for i in range(n+1)]      # creates a list of all positive integers up to n.
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):   # removes all multiples of p which by being a multiple...
                prime[i] = False             # ...makes them not prime.
        p += 1

    prime_list = []
    for p in range(2, n+1):      # this loop appends all the prime numbers to the empty list.
        if prime[p]:
            prime_list.append(p)

    return prime_list


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

    user_num = getint("Please enter a number: ")
    print(sieve_of_erasothenes(user_num - 1))


taskmanager()
