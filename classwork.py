#C:\Users\kaiba\cs introduction (you can delete it)\temperature-calculator-1\temperature-calculator\shit.py

fruit = ["apple", "banana", "orange", "apple", "strawberry"]
print(fruit)

# add an item to the list
fruit.append("pear")
print(fruit)

# get an index/position of an item in the list
print("index of apple: ", fruit.index("apple"))

# get a size of the list
print("number of elements in fruit: ", len(fruit))

# get the number of times an item appear in the list
print("count of apple: ", fruit.count("apple"))

fruit_dict = {'apples': 4, 'bananas': 3, 'strawberries': 10, 'oranges': 2}
print(fruit_dict)

fruit_dict['pears'] = 6
print(fruit_dict)

fruit_dict['apples'] += 1
print(fruit_dict)

to_list = list(fruit_dict)
print(to_list)

#sorting the elements alphabetical order
sorting = sorted(fruit_dict)
print(sorting)















