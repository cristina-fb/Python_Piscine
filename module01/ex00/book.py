import datetime

class book:
    def __init__(self, name):
        if type(name) != str:
            print("Invalid book! Book name must be a string.")
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if j.name == name:
                    print(name)
                    return j
        return None

    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Anade una receta al libro y actualiza last_update"""
        key = recipe.recipe_type
        self.recipes_list[key].append(recipe)
        self.last_update = datetime.datetime.now()