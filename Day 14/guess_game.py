# python | Day 14
# Guess the number
# You ask a user to guess a number between 1 and 50. The user has a maximum of 5 tries.
# If the user guesses wrongly, provide an error message indicating whether
# their guess was above or below the actual number.
# If the user guesses correctly, congratulate them and show the number of attempts they had.
# If the user exhausts all their tries, tell them they have exhausted their tries and end the game.
# E.G:
# > enter a number
# user: 1
# > wrong. the answer is greater than 1
# user: 25
# > wrong the answer is less than 25
# user: 14
# > wrong the number is greater than 14 user: 15
# > Correct! You got the right answer in 3 tries.

import random

highest = 50
answer = random.randint(1, highest)

attempts = 1
print(answer)

while attempts <= 5:
    guess = int(input("Please guess a number between 1 and {} OR zero(0) to QUIT: ".format(highest)))
    if guess == 0:
        print("Ouch! See you next time mate.")
        break
    elif (guess < answer) and (attempts < 5):
        print("Your guess was wrong, please guess higher.")
    elif (guess > answer) and (attempts < 5):
        print("Your guess was wrong, please guess lower.")
    elif guess == answer:
        print("Well done, you guessed it! congrats!!!")
        print("You guessed it correctly in {} attempt(s).".format(attempts))
        break
    attempts += 1
if attempts > 5:
    print("Sorry, your guesses were wrong and you've exhausted your five(5) attempts. Try again sometime.")
