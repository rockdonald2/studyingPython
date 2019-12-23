def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error, skip current call.")


print(div42by(0))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 2:
        print("That's a lot of cats")
    else:
        print("That's not that many cats")
except ValueError:
    print('Please enter a digit, not a transcript')


# Guess a number game
import random
print('I am thinking of a number between 1 and 50, you think you can guess it easily right? Then, let\'s play!')
randomNumber = random.randint(1, 50)

for guessesTaken in range(1, 11):
    print('Take a guess')
    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            print('Please enter a digit')
            continue

    if guess < randomNumber:
        print('Your guess is too low')
    elif guess > randomNumber:
        print('Your guess is too damn high')
    else:
        break  # current guess

if guess == randomNumber:
    print('Damn, you nailed it, good job!')
else:
    print('Damn')



