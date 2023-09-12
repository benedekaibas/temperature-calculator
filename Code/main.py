
def Main():
    
    print("Hi, this is a program that switches temperature between Fahrenheit and Celsius", end = "\n\n")

    user_input = str(input("What type of degree you want to switch?: " ))
    degree_input = int(input(f"You selected {user_input}, now type the degree in digits: "))

    #the two formulas for the calculation
    formula_c = ((degree_input) - 32) * 5/9 
    formula_f = (9/5 * (degree_input)) + 32

    #the process of deciding the user input and doing the calculation
    if user_input == "Fahrenheit":
        print(formula_c)
    elif user_input == "Celsius":
        formula_f = (9/5 * (degree_input)) + 32
        print(formula_f)
    else:
        print("You might misspelled the input!")
    
    
   # print(f"{formula} Celsius degrees.")


if __name__ == "__main__":
    Main()
