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

o = 0
for index in range(4):
    o += 25
    print("the value of the variable o is {0}".format(o))

name= "Aarya"
age= "14"
print("Hi, my name is {0}. I am {1} years old.".format(name, age))

import random
for x in range(1):
  print(random.randint(1,101))

  

