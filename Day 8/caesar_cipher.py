# python | Day 8
# Caesar Cipher
# A Caesar cipher is an ancient form of encryption. It involved taking a text(a string) as input,
# and encoding it by replacing each letter by the one n-steps  next to it in the alphabet.
# (E.G Shifting "Python" by 5, becomes "Udymts".—Note that this "shift", wraps around, which is why "y" becomes "d".).
# Task:
# "Write a function that takes in as parameters, a plaintext( string)to encode, and a _shift value _,
# and outputs the encoded value of the string.
# *Write another similar function that takes in the encoded string, with a shift_value, and decodes it.
# *Finally, write a third function that takes in a text, a shift value, and a third parameter
# to indicate whether to encode or decode the given text.(I.e f("string", 5, True/false) ) ,
# And print out the encoded(or decoded) text accordingly.

def encrypt(text, s):
    result = ""

    # iterating through text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase letters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(en_text, s):
    result = ""

    # iterating through text
    for i in range(len(en_text)):
        char = en_text[i]

        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Decrypt lowercase letters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def check_text(user_text, shift_value, en_de):
    if en_de.lower() == "encode":
        print("{}--> ".format(user_text) + encrypt(user_text, shift_value))
    elif en_de.lower() == "decode":
        print("{}--> ".format(user_text) + decrypt(user_text, 26 - shift_value))


plain_text = str(input("Please kindly enter your text: "))
shift = int(input("Please enter your shift value...MUST BE AN INTEGER!: "))
enc_dec = str(input("Do you want to 'encode' or 'decode' your text?: "))

check_text(plain_text, shift, enc_dec)
