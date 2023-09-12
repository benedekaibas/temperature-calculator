
def Main():
    
    print("Hi, this is a program that switches temperature between Fahrenheit and Celsius", end = "\n\n")

    user_input = int(input("Enter the temperature in Celsius (Only use numbers): "))

    formula = (user_input / (9/5)) + 32

    print(formula)
















if __name__ == "__main__":
    Main()
