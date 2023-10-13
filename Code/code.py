i = 0
start = 0 
end = 10


while i >= start and i < 10:
    i += 1
    print(f"{i} : {i}")


def range():
    set = start, end
    return set

for i in range():
    result = i - 1
    print(result)

a = 5 
b = int(input("input: "))

while a != b:
    try: 
        int(input("input again: "))
    except ValueError:
        print("The value you gave are not correct")










