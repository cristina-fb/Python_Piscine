class recipe:
    def __init__(self, name, lvl, time, ing, desc, rtype):
        if type(name) != str:
            print("Invalid recipe! Name is not a string.")
        else:
            self.name = name
        if type(lvl) != int:
            print("Invalid recipe! Cooking level is not an int.")
        else:
            self.cooking_lvl = lvl
        if type(time) != int:
            print("Invalid recipe! Cooking time is not an int.")
        else:
            self.cooking_time = time
        if type(ing) != list:
            print("Invalid recipe! Ingredients are not a list.")
        else:
            for i in ing:
                if type(i) != str:
                    print("Invalid recipe! Ingredients are not a string.")
            self.ingredients = ing
        if type(rtype) != str:
            print("Invalid recipe! Recipe type is not a string.")
        else:
            if rtype != 'starter' and rtype != 'lunch' and rtype != 'dessert':
                print("Invalid recipe! Recipe type must be starter, lunch or dessert.")
            else:
                self.recipe_type = rtype
        self.description = desc
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.name + " is a level " + str(self.cooking_lvl) + " recipe that takes " + str(self.cooking_time) + " minutes to make. You need the following ingredients: " + ", ".join(self.ingredients) + ". It is a good choice for " + str(self.recipe_type) + ".\n"
        if self.description != None:
            txt += self.description
        return txt