# python | Day 11
# Day 11: Euclid's algorithm(GCD).
# The GCD(Greatest Common divisor) of two numbers is the largest number by which both are divisible.
# E.G gcd(42, 18) is 6, since 6 is the highest common factor(HCF-same thing as GCD) of 42 and 18.
# Write a program that asks the user for two numbers and computes their GCD using Euclid's algorithm.
# The process is described below: *First, compute the remainder of dividing the larger number by the smaller one.
# *Next, replace the larger number with the smaller number, and the smaller number with the remainder.
# *Repeat this process until the smaller number equals zero. The GCD is the last value of the larger number.

def get_numbers(prompt):
    """ A function to get integer numbers from the user.

    This function will keep looping if the numbers are not integers
    until the user provides integers for integer numbers.
    """

    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")


def gcd_algo(x, y):
    """ A function to calculate the Greatest Common Divisor(GCD).

    This function uses Euclid's algorithm to calculate the GCD.It takes two integers(x and y) and then divides
    one by the other using the modulus operator.
    The remainder then becomes the new divisor dividing the second number.
    This process is repeated recursively till the divisor becomes zero(0) then the dividend value is returned.

    """
    if x == 0:
        return y
    return gcd_algo(y % x, x)


first_num = get_numbers("Please enter first number: ")
second_num = get_numbers("Please enter second number: ")
print("The Greatest Common Divisor(GCD) of {} and {} is {}."
      .format(first_num, second_num, gcd_algo(first_num, second_num)))
