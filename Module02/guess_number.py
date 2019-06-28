import random

print("-----------------------------")
print("   GUESS THAT NUMBER GAME")
print("-----------------------------")
print()

goal = random.randint(0, 100)
guess = -1

name = input("Player, what is your name? ")

while guess != goal:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)

    if guess < goal:
        print("Sorry {}, your guess of {} was too low.".format(name, guess))
    elif guess > goal:
        print("Sorry {}, your guess of {} was too high.".format(name, guess))
    else:
        print("Congratulations {}, you won! Your guess of {} was correct!".format(name, guess))

print("Done!")