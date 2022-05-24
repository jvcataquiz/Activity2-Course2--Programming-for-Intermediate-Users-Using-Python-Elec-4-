#1
from warnings import catch_warnings


x = 500
if x > 100:
    raise Exception("x is bigger than 100")
#2
try:
    print(variable_1)
except:
    print("variable_1 is not defined")

# 3

for i in range(6):
    print("I'm so happy")
#4
try:
    print(12 * 6)
except:
    print("This code contains an error")
else:
    print("This code has no error")

#5

best_burger = "Burger King"
number_2_burger = "Mcdonalds"

assert best_burger == "Burger King"
assert number_2_burger == "Mcdonalds"