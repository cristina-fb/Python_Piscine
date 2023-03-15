from recipe import recipe
from book import book

r1 = recipe("Cake", 3, 120, ["Flour", "Sugar", "Chocolate"], "Yummy!", "dessert")
r2 = recipe("Brownie", 2, 100, ["Flour", "Sugar", "Chocolate", "Almonds"], "My favourite one!", "dessert")
r3 = recipe("Salad", 1, 8, ["Lettuce", "Tomato", "Olive oil", "Vinegar"], "Easy peasy!", "starter")
r4 = recipe("Steak", 2, 10, ["Steak", "Salt"], None, "lunch")
r5 = recipe("Sushi", 10, 150, ["Rice", "Nori", "Salmon", "Tuna"], "From Japan!", "lunch")
b1 = book("Arguinano")
b1.add_recipe(r1)
b1.add_recipe(r2)
b1.add_recipe(r3)
b1.add_recipe(r4)
b1.add_recipe(r5)
lst = b1.get_recipes_by_types('dessert')
for i in lst:
    print(i.name)
print()
lst = b1.get_recipes_by_types('lunch')
for i in lst:
    print(i.name)
print()
lst = b1.get_recipes_by_types('starter')
for i in lst:
    print(i.name)
print()
print(b1.get_recipe_by_name("Sushi"))
print()
print(b1.get_recipe_by_name("Steak"))