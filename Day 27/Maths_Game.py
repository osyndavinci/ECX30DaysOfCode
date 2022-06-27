# python | Day 27
# Maths game.
# Using Python, create a game with the following rules:
# 1) A(randomly generated) basic algebraic
# expression is displayed onto the screen.(E.G 36×47, or 117 ÷ 9, etc.)
# 2) The user is required to provide an answer to the expression within 10 seconds.
# 3) If the user provides a RIGHT answer, he gains {10x(the number of seconds left)} points
# 4) If the user provides a WRONG answer,
# or the time elapsed, the player loses a life.
# 5) At the start of the game, the player provides his name, and begins playing with 3 lives.
# 6) The player loses once he has exhausted his 3 lives.
# Note:
# ~Only +,-,, operations are allowed. ~In the case of a division operation,
# the two numbers generated MUST be divisible.

import os
import random
import time
from time import perf_counter
from operator import add, sub, mul, truediv


def game(name):
    """A function for an arithmetic game."""

    print(f"Welcome to Maths Quiz {name}! You have ten(10) seconds to attempt a question, if your answer is correct, "
          f"\nyou will gain 10x(the number of seconds left) points. "
          f"\nYou have three(3) lives and will lose each life each time you fail a question or"
          f" each time you're timed out.")

    input("Please press Enter to start: ")

    lives = 3
    score = 0

    while lives >= 0:
        os.system("cls")
        time.sleep(2)
        operations = (add, sub, mul, truediv)
        operation = random.choice(operations)
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)

        if operation == add:
            print("What is", first_num, "+", second_num, "?")
            start_time = perf_counter()
            user_ans = int(input("Enter answer: "))
            end_time = perf_counter()
            time_left = 10 - (end_time - start_time)
            answer = operation(first_num, second_num)
            if user_ans == answer:
                score += time_left * 10
                print(f"Correct! You've gained {time_left * 10:0.0f} points!")
            else:
                print("Sorry, your answer is incorrect and thus, lost a life.")
                lives -= 1

        elif operation == sub:
            print("What is", first_num, "-", second_num, "?")
            start_time = perf_counter()
            user_ans = int(input("Enter answer: "))
            end_time = perf_counter()
            time_left = 10 - (end_time - start_time)
            answer = operation(first_num, second_num)
            if user_ans == answer:
                score += time_left * 10
                print(f"Correct! You've gained {time_left * 10:0.0f} points!")
            else:
                print("Sorry, your answer is incorrect and thus, lost a life.")
                lives -= 1

        elif operation == mul:
            print("What is", first_num, "*", second_num, "?")
            start_time = perf_counter()
            user_ans = int(input("Enter answer: "))
            end_time = perf_counter()
            time_left = 10 - (end_time - start_time)
            answer = operation(first_num, second_num)
            if user_ans == answer:
                score += time_left * 10
                print(f"Correct! You've gained {time_left * 10:0.0f} points!")
            else:
                print("Sorry, your answer is incorrect and thus, lost a life.")
                lives -= 1

        elif operation == truediv:
            checker = first_num % second_num
            if checker == 0:
                print("What is", first_num, "/", second_num, "?")
                start_time = perf_counter()
                user_ans = int(input("Enter answer: "))
                end_time = perf_counter()
                time_left = 10 - (end_time - start_time)
                answer = first_num // second_num
                if user_ans == answer:
                    score += time_left * 10
                    print(f"Correct! You've gained {time_left * 10:0.0f} points!")
                else:
                    print("Sorry, your answer is incorrect and thus, lost a life.")
                    lives -= 1
            else:
                continue

        if lives == 0:
            print(f"Well done {name}! You have exhausted you three(3) lives."
                  f"Your final score is {score:0.0f} point(s)."
                  f"See you soon!")
            break


def game_manager():
    user_name = str(input("Please enter your name: "))
    game(user_name)


game_manager()
