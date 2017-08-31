# Create a function for one dice
from random import randint


def die_roll():
        sides = int(input('How many sides are there to this die? '))
        print("You rolled a {} out of {}".format(randint(1,sides), sides))
        pass


def dice_rolls():
    times = int(input('How many dice would you like to roll? '))
    ran = 0
    while times > ran:
        print(die_roll())
        ran += 1
    else:
        print('\n''Thanks for playing!')


dice_rolls()
