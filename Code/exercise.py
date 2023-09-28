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

def main():

    #Define the "constants" (given measurements) provided
    #       in the README; add comments defining each group
    def rectangle(width, length):
        a = width * length
        return a 

    def triangle(leg):
        a = (leg**2)
        return a 

    def square(a):
        result = a * a 
        return result

    def circle(r):
        pi = math.pi
        result = pi * 4 * r 
        return result

#these are the functions for the different parts of the house 
    def longerWall():
        longer = rectangle(27, 7) * 2 
        return longer
    print(longerWall())
    def shorterWall():
        result = rectangle(18, 7) * 2 
        return result
    print(shorterWall())
    def floor():
        result = rectangle(18, 27)
        return result
    print(floor())
    def gables():
        result = triangle(12.73) * 18 * 1/2
        return result
    print(gables())
    def roofing():
        result = rectangle(12.73, 27) * 2
        return result
    print(roofing())
    def windows():
        result = rectangle(8, 3) * 6 
        return result 
    print(windows())
    def entryway():
        result = square(5)
        return result
    print(entryway())
    def Allowance_For_Tree():
        result = circle(4)
        return result
    print(Allowance_For_Tree())

    total = longerWall() + shorterWall() + floor() + gables() + roofing() + windows() + entryway() + Allowance_For_Tree()

    print(f"This is total: {total}")

if __name__ == "__main__":
    main()

