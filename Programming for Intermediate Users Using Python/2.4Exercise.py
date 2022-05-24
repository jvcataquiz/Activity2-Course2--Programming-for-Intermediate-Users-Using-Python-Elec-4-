flavors = ["vanilla", "chocolate","strawberry","cookies and cream", "bubblegum"]
toppings = ["almonds","banana slices","chocolate syrup", "caramel syrup","white chocolate chips"]

iced_cream = dict(zip(flavors, toppings))

print(iced_cream)

iced_cream["chocolate"] = "blueberries"
print(iced_cream)

iced_cream.update({"matcha":"pistachios", "ube":"mango slices"}) 
print(iced_cream)