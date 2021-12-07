# "A number guessing game"

# # put your code here

import random

# question = input('this thing on?')
# if question == ('yes'):
#     print('yes')
# else:
#     print('no')

name = input('What is your name?')
print('Hello, ' + name)
number = random.randint(1, 100)
print(number)
print(name + ', I\'m thinking of a number between 1 and 100.')
print('Try to guess my number.')

guess = int(input('Your guess?'))
if guess == number:
    print('Well done,' + name + '! You found my number in 1 try!')
else:
    if(guess > number):
        print('Your guess is too high, try again.')
    elif(guess < number):
        print('Your guess is too low, try again.')
    guesses = 1
    while(guess != number):
        guess = int(input('Your guess?'))
        guesses += 1
        if guess == number:
            guesses = str(guesses)
            print('Well done, ' + name + '! You found my number in ' + guesses + ' tries!')
        else:
            if(guess > number):
                print('Your guess is too high, try again.')
            elif(guess < number):
             print('Your guess is too low, try again.')


