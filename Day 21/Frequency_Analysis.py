# python | Day 21
# Frequency analysis.
# 1) Write a function that takes a string as input and:
# Returns a dictionary whose keys are the characters found in the text, and whose values are the number
# of occurrences of that character in the text. E.G: f("It is good!") =>
# {"I": 2, "t": 1, "s": 1, "g":1, "o":2, "d":1,"!":1}

# 2)Write ANOTHER function that takes an input string and returns a dictionary whose keys are the words in the text,
# and whose values are the respective frequencies of these words.
# E.G: f("It is not good, is it?") => {"It": 2, "is": 2, "not": 1, "good":1}
# Note: In both cases, disregard case sensitivity.


import string


def char_analysis(user_str):
    """ A function to count the number of occurrences of characters in a string and return them as dictionary values.
    The characters become the keys while the number of occurrences are the values.
    """

    freq_dict = {}

    for char in user_str.lower():    # .lower() is used to avoid case sensitivity.
        if char in freq_dict and char != " ":
            freq_dict[char] += 1
        elif char not in freq_dict and char != " ":
            freq_dict[char] = 1

    return freq_dict


def words_analysis(user_str):
    """ A function to count the number of occurrences of words in a string and return them as a dictionary values.
    The words become the keys while the number of occurrences are the values. Also, punctuations are stripped off
    from the words.
    """

    freq_dict = {}

    for word in user_str.lower().split(" "):
        for char in word:
            if char in string.punctuation:
                word = word.strip(char)

        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict


def taskmanager():
    input_str = str(input("Enter a text: "))
    print(char_analysis(input_str))
    print(words_analysis(input_str))


taskmanager()
