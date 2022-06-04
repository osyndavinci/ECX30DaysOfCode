# python | Day 4
# Decimal to Hexadecimal
# Without using the inbuilt hex() function, write a function that takes an integer as input,
# # and prints out its conversion to Hexadecimal as output

input_dec = int(input("Please enter the decimal value you plan to convert to hex: "))
# get a value of decimal from the user


def dec_2_hex(dec_num):
    """ A function to convert a decimal to a hexadecimal.
    This function returns ret_value.

    ret_val(str):  initialized as an empty string. calls the gethexachar() function and recurs.
    hexa_value(int): gets the modulus remainder of dec_num.
    dec_num(int): the parameter value of input_dec. It's final value is an integer division by 16.

    """
    ret_value = str()
    while dec_num > 0:
        hexa_value = dec_num % 16
        dec_num = dec_num // 16
        ret_value = gethexchar(hexa_value) + ret_value

    return ret_value


def gethexchar(dec_digit):
    """ A function to get the equivalent value of the modulus remainder in hexagonal.

    The function returns values 1,2,...,9 if the remainder is between 1,2,...,9.
    It however returns A,B,C,D,F when the remainder value is 10,11,12,13,14,15 respectively.

    dec_digit(int): parameter equivalent of the modulus remainder.
    dec_dict(dict): stores the strings A-F in a dictionary and is accessed by keys which are numbers 10-15.
    dec_str(str): gets the str value when the dict key is used.
    """

    if dec_digit < 10:
        return str(dec_digit)
    elif dec_digit >= 10:
        dec_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        dec_str = dec_dict[dec_digit]
        return dec_str


print(input_dec, "is equal to ", dec_2_hex(input_dec), " in hexadecimal.")
# prints the output we need
