# python | Day 16
# When in Rome.
# *Write a function that takes an integer as input, and returns its translation to Roman numerals.
# *Using the aforementioned function, write a program that takes user input and prints out their Roman numeral form.
# This program must include all necessary type checks or Exception handling

import sys


def convert_to_roman(num):
    """ A function to convert Hindu-Arabic numbers to Roman Numerals."""

    result = ""
    roman_table = [
                 (1000, "M"), (900, "CM"),
                 (500, "D"), (400, "CM"),
                 (100, "C"), (90, "XC"),
                 (50, "L"), (40, "XL"),
                 (10, "X"), (9, "IX"),
                 (5, "V"), (4, "IV"),
                 (1, "I"),
                 ]

    for digit, roman in roman_table:
        i, remainder = divmod(num, digit)
        result += roman * i
        num = remainder
    return result


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
        except EOFError:
            sys.exit(0)


def taskmanager():
    """ This function runs the program by calling the functions above."""

    user_num = getint("Please enter a number: ")
    output_value = convert_to_roman(user_num)
    print(output_value)


taskmanager()
