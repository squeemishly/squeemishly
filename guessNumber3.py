'''
Change from version 2:
add numbGuesses to track how many guesses it takes to get the right number
add +1 to numbGuesses for every wrong guess
say how many guesses it took to get the right number
'''

import random

def guessNumb():
    start = int(input("give me a low number"))
    end = int(input("give me a high number"))
    newNumb = random.randint(start,end)
    numbGuesses = 1
    wrong = True
    userGuess = input("Guess a number between %d and %d" %(start,end))
    while wrong == True:
        if int(userGuess) < newNumb:
            numbGuesses += 1
            print("Your guess is too low.")
            userGuess = input("Guess again.")
        elif int(userGuess) > newNumb:
            numbGuesses +=1
            print("Your guess is too high.")
            userGuess = input("Guess again.")
        else:
            print("You guessed it!")
            print("It took you %i guesses to get it" %numbGuesses)
            wrong = False

guessNumb()
