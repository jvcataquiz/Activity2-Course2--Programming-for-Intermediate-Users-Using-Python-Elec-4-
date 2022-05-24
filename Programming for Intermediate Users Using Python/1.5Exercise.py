class Customers:
    greetings = "Welcome to Coffe Palace!!"
    def __init__(self,name,beverage,food,total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
c_1 = Customers("Nate","Espresso","Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino","Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon Roll", 225)
c_4 = Customers("Jerry","Caramel Macchiato","Glaze Doughnut",230)
c_5 = Customers("Paz","Iced Tea", "Blueberry Pancakes", 315)

print(Customers.greetings)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)