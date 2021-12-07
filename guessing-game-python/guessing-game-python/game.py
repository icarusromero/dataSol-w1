# "A number guessing game"

# # put your code here

import random

def check_if_int(initguess):
    while type(initguess) != "int":
        try:
            x = int(initguess)
        except:
            print(initguess + ' isn\'t a number idiot.')
            initguess = input('Your guess?')
        else:
            initguess = int(initguess)
            break
    guess = initguess
    return guess

name = input('What is your name?')
print('Hello, ' + name)
number = random.randint(1, 100)
print(number)
print(name + ', I\'m thinking of a number between 1 and 100.')
print('Try to guess my number.')

initguess = input('Your guess?')

guess = check_if_int(initguess)


if guess == number:
    print('Well done,' + name + '! You found my number in 1 try!')
else:
    if guess < 1 or guess > 100:
        print('Thought you could get away with an out of range number, sweaty? I don\'t think so :)).')
    elif(guess > number):
        print('Your guess is too high, try again.')
    elif(guess < number):
        print('Your guess is too low, try again.')
    guesses = 1
    while(guess != number):
        guess = input('Your guess?')
        guess = check_if_int(guess)

        guesses += 1
        if guess < 1 or guess > 100:
            print('Thought you could get away with an out of range number, sweaty? I don\'t think so :)).')
        elif guess == number:
            guesses = str(guesses)
            print('Well done, ' + name + '! You found my number in ' + guesses + ' tries!')
        else:
            if(guess > number):
                print('Your guess is too high, try again.')
            elif(guess < number):
                print('Your guess is too low, try again.')


