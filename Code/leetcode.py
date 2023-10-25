#path to this file
#C:\Users\kaiba\cs introduction (you can delete it)\temperature-calculator-1\temperature-calculator\Code\leetcode.py


import random
numbers_x = [0,1,2,3,4,5,6,7,8,9,10]
numbers_y = [0,1,2,3,4,5,6,7,8,9,10]

x = random.choice(numbers_x)
y = random.choice(numbers_y)
x_two = random.choice(numbers_x)
y_two = random.choice(numbers_y)
#this part checks if the first and second elements are actually correct
random_coordinate = x, y
"""
print(random_coordinate)
print(random_coordinate[0])
print(random_coordinate[1])
"""
#defining global variables so
global X 
global Y 
global X_TWO
global Y_TWO
X = x
Y = y
X_TWO = x_two
Y_TWO = y_two
#check if the global variables work
print("\n", X, Y, "\n", X_TWO, Y_TWO)
#user input

def calculation():
    user_x = int(input("Enter coordinate x: "))
    user_y = int(input("Enter coordinate y: "))
    #store = user_x, user_y
    return user_x, user_y
def in_between()
    calculation()
    #test_x = user_x this does not work 
    if x <= test_x <= x_two or x_two <= test_x <= x:
        print("Your x value is between the endpoints.")
    else:
        print("Your x value is not between the endpoints")

    
print(in_between())









