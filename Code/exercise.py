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

"""

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

def triangle(base,leg):
    a = base * (leg**2)
    return a 

def square(a):
    result = a * a 
    return result

def circle(r):
    pi = math.pi
    result = pi * 4 * r 
    return result

#NOW WE USE THE FUNCTIONS INSIDE THE HOUSE PARTS' FUNCIONS

def walls():
    wall_one = rectangle(18, 7)
    wall_two = rectangle(27, 7)
    result = wall_one, wall_two
    return result

def floor():
    result = rectangle(18 * 27)
    return result

def gables():
    result = triangle(18, 12.73)
    return result

print(f"{gables(): .{1}f}")

def roofing():
    result = rectangle(12.73, 27)
    return result

def windows():
    result = rectangle(8, 3)
    return result 

def entryway():
    result = square(5)
    return result

print(entryway())

def Allowance_For_Tree():
    result = circle(4)
    return result

print(Allowance_For_Tree())


#checking if the allowance_for_tree gives back the right value
pi = math.pi
r = 4
result = pi * r**2
print(result)






