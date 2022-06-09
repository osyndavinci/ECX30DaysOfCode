# python | Day 9
# Is Prime
# Task: Write a function  that takes an integer as input,
# and determines whether it is a prime number or not.

def isprime():
    """ A function to check whether a number is Prime or not.

    user_num(int): gets the number from the user.
    0 and 1 are not considered as prime numbers therefore the last else statement.
    If the user_num is greater tha 1, the function iterates from 2 up to half of user_num + 1.
    Half of user_num is chosen because the highest factor of an integer apart from itself is
    less than or equal to half of the integer.
    The "+1" is added to include this half.

    """

    user_num = int(input("Please enter your number: "))

    if user_num > 1:
        for i in range(2, int(user_num / 2) + 1):
            if (user_num % i) == 0:
                print(user_num, "is not a prime number.")
                break
        else:
            print(user_num, "is a prime number.")

    else:
        print(user_num, "is not a prime number.")


isprime()
