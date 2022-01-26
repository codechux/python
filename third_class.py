#   LIST METHODS  ##

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(color_list.index('Red'))

# choice = input("Enter your favourite colors:\n>")

# color_list.append(choice)


# position = int(input("Enter the position:\n>"))
# color_list.insert(position, choice)
# Join = choice.split()
# color_list.extend(Join)

# print(color_list)

li = [0, 2, 9, 8]
a = li.pop(1)
li.append(a)

print(li)

# TUPLES

my_tuples = (1,)
my_tuples1 = 1, 2, 3, 4, 5, 6

print(type(my_tuples))
print(type(my_tuples1))

a = {1, 3, 4, 6}
b = {7, 8, 9, 2}

# c = a.union(b)

eng = input("Enter for eng\n>")
fre = input("Enter for french\n>")

english_list = eng.split()
french_list = fre.split()

engSet = set(english_list)
freSet = set(french_list)

total = engSet.symmetric_difference(freSet)
print(len(total))
