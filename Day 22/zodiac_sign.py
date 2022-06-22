# python | Day 22
# Zodiac.
# Extend the function from day 19 to return BOTH the day of the week AND
# the corresponding "Zodiac sign" of the input date.
# Return value can be a list or ANY convenient structure. All rules relating to task 19 still apply.
# (See more on Western astrological signs.).

import string
import calendar


def zodiac_sign(day, month):
    """ A function to return the zodiac sign of a date using day and month as augments."""

    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

    return astro_sign


def get_day():
    """ A function to check the day of the week from a date."""

    while True:
        try:
            # collects the date from the user.
            user_date = str(input("Please enter a date in 'ddmmyy' or 'yymmdd' format,"
                                  " \nuse a separator(a space or a punctuation)"
                                  " \nin-between each part(e.g. 22-12-2012 or 2012-12-22): "))

            if " " in user_date:          # checks if a space is used as a separator.
                date = user_date
            else:                         # checks the separator, removes it and replaces it with a space.
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
                zodiac = zodiac_sign(day, month)
                return days[day_index], zodiac

            else:       # else, it is yymmdd format.
                year, month, day = (int(i) for i in date.split(" "))
                day_index = calendar.weekday(year, month, day)
                days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
                zodiac = zodiac_sign(day, month)
                return days[day_index], zodiac

        except ValueError:
            print("Invalid date entered, please try again. Make sure you include a separator.")


def process_userinput():
    final_day, zod_sign = get_day()
    print("\nThe day is {} and the zodiac sign is {}.".format(final_day, zod_sign))


process_userinput()
