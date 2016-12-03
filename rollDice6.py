'''
Changes from version 4:
total the damage rolled with the dice
'''

import random


def rollDice():
    sides = int(input("How many sides do your dice have?"))
    i = random.randint(1,sides)
    print("You rolled a " + str(i))
    return(i)


def DND():
    rolling = True
    damage = 0
    while rolling == True:
        numDice = int(input("How many dice do you have?"))
        for x in range (0, numDice):
            roll = rollDice()
            damage += roll
        bonus = int(input("Did you do any additional damage?"))
        damage += bonus
        print("Total Damage: ", damage)
        ask = input("would you like me to roll the dice again?")
        if ask.lower() == "yes" or ask.lower() == "y":
            rolling = True
        else:
            rolling = False


DND()
