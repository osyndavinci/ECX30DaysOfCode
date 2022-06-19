# python | Day 19
# Write a function that takes in a date as input, and returns what day of the week it is.
# *The input date can be in any convenient format(Whether a "ddmmyy" string, a series of integers, etc)
# *Your function must work for both future and past dates.
# *Exception handling(or Type checking) is necessary.


import string
import calendar


def get_day():
    """ A function to check the day of the week from a date."""

    while True:
        try:
            # collects the date from the user.
            user_date = str(input("Please enter a date in 'ddmmyy' or 'yymmdd' format,"
                                  " use a separator(a space or a punctuation) in-between each part: "))
            if " " in user_date:      # checks if a space is used as a separator.
                date = user_date
            else:                    # checks the separator, removes it and replaces it with a space.
                date_split = ""
                for i in user_date:
                    if i in string.punctuation:
                        date_split = user_date.split(str(i))
                date = " ".join(date_split)

            date_list = date.split(" ")       # splits the date again.

            if len(date_list[0]) < 3:         # checks the date format. if the digit is less than 3, then it is ddmmyy.
                day, month, year = (int(i) for i in date.split(" "))
                day_index = calendar.weekday(year, month, day)
                days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
                return days[day_index]

            else:       # else, it is yymmdd format.
                year, month, day = (int(i) for i in date.split(" "))
                day_index = calendar.weekday(year, month, day)
                days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
                return days[day_index]

        except ValueError:
            print("Invalid date entered, please try again. Make sure you include a separator.")


def process_userinput():
    final_day = get_day()
    print("\nThe day is {}.".format(final_day))


process_userinput()
