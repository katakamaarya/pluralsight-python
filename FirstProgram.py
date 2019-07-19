food_names = ["blueberry", "chocolate", "pizza", "ice cream"]

print(food_names)
print(food_names[1:])
print(food_names[2])
food_names.append("tacos")
print(food_names)
print(len(food_names))
del food_names[3]
print(food_names)
for name in food_names:
    print("Food name is {0}".format(name))

o = 5
for index in range(25):
    o += 25
    print("the value of the variable o is {0}".format(o))



