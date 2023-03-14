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

def add_recipe(cookbook):
    name = input("Enter a recipe name: >>\n")
    ingredients = []
    print("Enter ingredients: >>")
    while True:
        try:
            ingredients.append(input())
        except:
            break
    meal = input("Enter a meal type: >>\n")
    try:
        prep_time = input("Enter a preparation time: >>\n")
    except:
        print("Sorry, not a valid time")
        return
    recipe = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }
    cookbook[name] = recipe

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
    try:
        op = input("Please select an option:\n>> ")
        n = int(op)
    except:
        print("Sorry, this option does not exist.\n")
        continue
    if n == 1:
        add_recipe(cookbook)
    elif n == 2:
        try:
            name = input("Please enter a recipe name to delete:\n>> ")
            del_recipe(cookbook, name)
        except:
            print("Sorry, that recipe is not on the cookbook.\n")
    elif n == 3:
        try:
            name = input("Please enter a recipe name to get its details:\n>> ")
            print_details(cookbook[name], name)
        except:
            print("Sorry, that recipe is not on the cookbook.\n")
    elif n == 4:
        print_names(cookbook)
    elif n == 5:
        print("Cookbook closed. Goodbye !")
        sys.exit()
    else:
        print("Sorry, this option does not exist.\n")

