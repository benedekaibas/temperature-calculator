import math


"""user_num = int(input("Enter a number: "))
user_power = int(input("Enter a power: "))

def calculation(num, power):
    num = user_num
    power = user_power

    result = num ** power
    return result

print(calculation(user_num, user_power))"""




#---------------------------------------------------------#

"""def walls():
    parameters = [18, 7, 27, 7]
    wall = parameters[0] * parameters[1]
    wall_two = parameters[2] * parameters[3]
    final = wall, wall_two
    return final

print(walls())

#function that calculates the floor

def floor():
    a = 18
    b = 27
    return a * b 

print(floor())

#function that calculates the gables

def gables():
    base = 18
    leg_one = 12.73
    leg_two = 12.73
    triangle = base * leg_one * leg_two
    return triangle 

print(gables())

#function that calculates roofing 

def roofing():
    a = 12.73
    b = 27
    return a * b

print(roofing())

#function that calculates windows

def windows():
    a = 8 
    b = 3
    return a * b

print(windows())

#function that calculates entryway

def entryway():
    a = 5**2
    return a 

print(entryway())

# function that calculates allowance for tree

def Allowance_For_Tree():
    #the equations is A = pi * r**2
    pi = math.pi
    radius = 4 
    final = pi * radius**2
    return final 

print(Allowance_For_Tree())"""

def rectangle(width, length):
    a = width * length
    return a 

def triangle(base, leg_one, leg_two):
    a = base * leg_one * leg_two
    return a 


#this is a sample that how can I call the rectangle function for other functions
def fal():
    result = rectangle(18, 18)
    return result 
    
print(fal())

def triangle(leg):
    a = 1/2 * (leg**2)
    return a 

def square(a):
    result = a * a 
    return result

def circle(pi, r):
    pi = math.pi
    result = pi * 4 * r 
    return result








