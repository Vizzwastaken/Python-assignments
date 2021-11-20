
import random
guess = ''

print('Guess the coin toss! Enter heads or tails:')
guess = int(input())
toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(guess)
print(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
