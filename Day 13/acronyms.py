# python | Day 13
# What's the acronym(s)?
# Ask the user to enter a sentence with an acronym or more,
# and you'll return--and--print all the acronyms in the sentence.
# Input -> "I need to get this done ASAP." Output -> "ASAP"
# input -> "SMH. The NPF is really a joke." Output -> "SMH NPF"
# input -> "LOOOL. I thought you were at KFC." Output -> "LOOOL KFC"
# (Note: An "acronym", for our purposes, is defined as any continuous sequence of uppercase letters)


def find_acronym():
    """ A function to print acronym(s) in a sentence.

    user_sentence(string):this variable collect a text from the user and is stored as a string.
    acronym_list(list): this uses conditional list comprehension to evaluate
    the user's text accordingly with the given task.
    acronym_string(string): this as the name implies converts lists in acronym_list to a string
    using the .join() function and a space to join them and is then printed.

    """

    user_sentence = str(input("Enter a sentence containing an acronym or more: "))

    acronym_list = [word.strip(".") for word in user_sentence.split(" ") if (word.isupper() and len(word) > 1)]

    acronym_string = " "

    acronym_string = acronym_string.join(acronym_list)
    print(acronym_string)


find_acronym()
