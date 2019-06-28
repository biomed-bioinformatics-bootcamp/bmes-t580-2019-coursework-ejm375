import random

print("-----------------------------")
print("   GUESS THAT PRIMER GAME")
print("-----------------------------")
print()

goal = random.choice("ACGT")
for i in range(4):
    goal += random.choice("ACGT")

guess = "NNNNN"

name = input("Player, what is your name? ")

while guess != goal:
    guess = input("Guess a 5 base pair primer: ")

    misses = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            misses += 1

    if misses > 0:
        print("Sorry %s, you guessed %i bases wrong. Play again?" % (name, misses))

    else:
        print("Congratulations %s, you won! Your guess was correct!" % name)

print("Done!")