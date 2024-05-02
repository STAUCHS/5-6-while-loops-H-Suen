# Example 4 - Guessing Game - Correct Solution
import random

rand_num = random.randrange(1, 101)

guess = int(input('Input a guess: '))

while guess != rand_num:
    if guess > rand_num:
        print('Too high!')
    else:
        print('Too low!')
    guess = int(input('Input a guess: '))

print('Congratulations! You guessed correct!')