import random 

lower = 1
upper = 10
takeGuess = int(input("Take a guess: "))
guess = random.randint(lower, upper)

def lower():
    return takeGuess < guess

def upper():
    return takeGuess > guess

while (takeGuess != guess):
    #takeGuess = int(input("Take a guess: "))
    if (takeGuess != guess and lower() == True):
        print("You did not find the number, plus your guessed number is under the secret number!")
        takeGuess = int(input("Take a guess: "))
    elif (takeGuess != guess and upper() == True):
        print("You did not find the number, plus your guessed number is above the secret number! ")
        takeGuess = int(input("Take a guess: "))
    elif (takeGuess != guess and upper() == False and lower() == False):
        print("You are outside of the range")
        takeGuess = int(input("Take a guess: "))
    else:
        print("Your input is wrong!")

while (takeGuess == guess):
    print("Congrats, you won this game!")
    newGame = str(input("Do you want to play another game? Y / N:"))
    if newGame == "Y":
        takeGuess = int(input("Take a guess: "))
    elif newGame == "N":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, but your input was wrong!")


    
    



    









