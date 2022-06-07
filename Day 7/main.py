# python | Day 7
# Wordle
# Task: Make a Wordle game.
# Description: Wordle is a single player game,
# in which a user is required to guess a 5-letter hidden word in 6 Attempts.
# *The user makes a first guess.( E.G: "Skate").
# * Print out a progress guide, like this. "√××√+",
# * "√" Indicates that the letter at that position was guessed correctly.
# * "+" indicates that the letter at that position is in the hidden word, but in a different position.
# *"×" indicates that the letter at that position is wrong, and isn't in the hidden word.
# *This process is repeated until the user either guesses the hidden word correctly—in which case,
# he Wins!—, or exhausts his 6 Attempts, losing.
# *The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.


import random
import json


def game_instructions():
    print("""Wordle is a single player game; A player has to guess a five letter hidden word.
You have six attempts.
Your Progress Guide is "✔❌❌✔➕".
"✔" Indicates that the letter at that position was guessed correctly.
"➕" indicates that the letter at that position is in the hidden word, but in a different position.
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word.  """)


game_instructions()

f = open('words.json')
words = json.load(f)
pos_word_bank = words['words']


def review_word():
    hidden_word = random.choice(pos_word_bank)
    attempt = 6
    while attempt > 0:
        user_guess = str(input("\n Guess our WORDLE word for the day: "))
        if user_guess == hidden_word:
            print("You guessed the word correctly! Congratulations!!! WIN!! 🕺🕺🕺 ")
            break
        else:
            attempt -= 1
            print("Sorry your guess is WRONG, try again...")
            print("You have {} attempts remaining...".format(attempt))
            for char, word in zip(hidden_word, user_guess):
                if word in hidden_word and word in char:
                    print(word + "✔", end=" ")
                elif word in hidden_word:
                    print(word + "➕", end=" ")
                else:
                    print(word + "❌", end=" ")
            if attempt == 0:
                print("\nGame over !!!! \n Sorry you finished your attempts.")


review_word()
f.close()
