# python | Day 18
# Reverse order.
# Write a function that takes a string as input, and returns a string similar to the input,
# but with the words in reverse order, and the punctuation marks maintaining their original order.
# E.G:
# f("Hello. I'm Edwin A.J, and you?") => "You and. A.J Edwin I'm, Hello?"
# f("What time is it? Hammer time.") => "Time Hammer? It is time what."
# Note: As shown in the example above, the order of the punctuation marks("?", ",", ".") have not changed.
# Only the words have.


import re


def uppercase(matchobj):
    return matchobj.group(0).upper()


def capitalize(s):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)


def reverse(string):
    """
    Function 'reverse' takes a string as input and returns a reversed order with the punctuation marks maintaining their original order.
    """
    if not isinstance(string, str):
        return "Invalid input."

    last_punc = string[-1]
    if last_punc.isalpha():
        return "Punctuate your sentence properly."

    string = string[0:-1]
    new_string = []
    last_index = [0]
    punc = []
    for index, char in enumerate(string):
        # If a space following a punctuation is observed
        if not char.isalpha() and string[index+1] == " ":
            new_string.append(string[last_index[-1]:index])
            punc.append(string[index:index+2])
            last_index.append(index+2)

    new_string.append(string[last_index[-1]:])
    for index, str_ in enumerate(new_string):
        # Reverses word per portion
        new_string[index] = " ".join(str_.split()[::-1])

    # Reverses string
    new_string = new_string[::-1]
    new_string[-1] = new_string[-1].lower()

    final = ""
    for i in range(len(punc)):
        final += new_string[i]
        final += punc[i]

    final += new_string[-1]
    final += last_punc
    return capitalize(final)


def taskmanager():
    """ This function runs the program by calling the functions above."""

    user_text = reverse(str(input("Please enter a text of strings: ")))
    print(user_text)


taskmanager()
