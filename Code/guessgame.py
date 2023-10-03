import random 

lower = 1
upper = 5
takeGuess = int(input("Take a guess: "))
guess = random.randint(lower, upper)

def lower():
    return takeGuess < guess

def upper():
    return takeGuess > guess

while True:
    if (takeGuess != guess and lower() == True):
        print("You did not find the number, plus you guessed number is under the secret number!")
    elif (takeGuess != guess and upper() == True):
        print("You did not find the number, plus your guessed number is above the secret number! ")
    else:
        print("You guessed the number!")
    break











