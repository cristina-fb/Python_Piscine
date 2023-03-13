import sys
def print_op():
    print("List of available option:")
    print(" 1: Add a recipe")
    print(" 2: Delete a recipe")
    print(" 3: Print a recipe")
    print(" 4: Print the cookbook")
    print(" 5: Quit")

def print_names(cookbook):
    print("Cookbook recipes:")
    for i in cookbook:
        print("- " + i)

def print_details(recipe, name):
    print("Recipe for " + name + ":")
    print(" Ingredients list: " + str(recipe['ingredients']))
    print(" To be eaten for: " + recipe['meal'] + ".")
    print(" Takes " + str(recipe['prep_time']) + " minutes of cooking.")

def del_recipe(cookbook, recipe):
    del cookbook[recipe]

def add_recipe(cookbook, name, ingredients, meal, prep_time):
    cookbook[name] = {ingredients, meal, prep_time}

sandwich = {
    'ingredients': ['ham', 'bread', 'cheese', 'tomato'],
    'meal': 'lunch',
    'prep_time': 10
}
cake = {
    'ingredients': ['flour', 'sugar', 'egss'],
    'meal': 'dessert',
    'prep_time': 60
}
salad = {
    'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
    'meal': 'lunch',
    'prep_time': 15
}

cookbook = {
    'sandwich': sandwich,
    'cake': cake,
    'salad': salad
}

print("Welcome to the Python Cookbook !")
while 1:
    print_op()
    op = input("Please select an option:\n>> ")
    if op == 1:
        add_recipe(cookbook, 'sandwich', ['ham', 'bread', 'cheese', 'tomato'], 'lunch', 10)
    elif op == 2:
        del_recipe(cookbook, 'sandwich')
    elif op == 3:
        name = input("Please enter a recipe name to get its details:\n>> ")
        print_details(cookbook['sandwich'], 'sandwich')
    elif op == 4:
        print_names(cookbook)
    elif op == 5:
        print("Cookbook closed. Goodbye !")
        sys.exit()
    else:
        print("Sorry, this option does not exist.")

