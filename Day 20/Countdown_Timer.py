# python | Day 20
# Countdown Timer.
# Write a program that:
# 1) Asks the user to enter a time period in the form of a number with a unit of either seconds, minutes,
# or hours. (E.G "44s", "32m", "10h".) *the last character of the string entered would be used to determine its unit.
# 2) Counts down from the input value, and prints out the time left on the clock every second.
# 3) When the time is exhausted, makes a beeping sound non-stop until the user exits the app.
# For example: T>Enter a time
# User> 5s
# T>5 seconds left
# >4 seconds left
# >3 seconds left
# >2 seconds left
# >1 second left
# *continuous indefinite beeping*
# (Hint: A "beeping sound" can be achieved using the "bell character", or any library of your choice.)


import time
import winsound


def countdown_timer():
    """ A countdown function."""

    while True:       # will run the program if the exception is handled.
        try:
            user_time = str(input("Enter a time to countdown from: "))   # collects the time to countdown.
            frequency = 250              # frequency of the Beep per duration.
            duration = 1000              # the duration of the beep sound.

            # this block of codes checks the unit of the time entered.
            if user_time[-1].lower() == "s":
                user_time = int(user_time[:-1])
            elif user_time[-1].lower() == "m":
                user_time = int(user_time[:-1]) * 60
            elif user_time[-1].lower() == "h":
                user_time = int(user_time[:-1]) * 3600

            # this blocks of codes divide the user_time using the divmod() function.
            while user_time:        # continues running till user_time is zero(0).
                mins, secs = divmod(user_time, 60)
                hours, mins = divmod(mins, 60)
                timer = '{:02d} hours:{:02d} minutes:{:02d} seconds left'.format(hours, mins, secs)
                print(timer, end="\n")
                time.sleep(1)
                user_time -= 1

            while True:       # this makes the sound continuous until the user stops the program.
                winsound.Beep(frequency, duration)

        except TypeError:
            print("Invalid unit entered. Please use 's' for seconds eg. 44s,"
                  " 'm' for minutes eg. 21m, and 'h' for hours eg. 10h.")
        except ValueError:
            print("Invalid unit entered. Please use 's' for seconds eg. 44s,"
                  " 'm' for minutes eg. 21m, and 'h' for hours eg. 10h.")


countdown_timer()
