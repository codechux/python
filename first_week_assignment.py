my_list = ["The", "quick", "brown", "fox",
           "jumps", "over", "the", "lazy", "dog."]

list1 = " ".join(my_list)

print(list1)

new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4] = False

print(new_list)

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list2 = list[1:4]

print(list2)

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = input("Enter your favourite color:\n ")

color_list.append(color)
print(color_list)
