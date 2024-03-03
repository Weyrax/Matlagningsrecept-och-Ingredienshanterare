class RecipeManager:
    def __init__(self):
        # Skapar en dictionary för att lagra recept, där varje receptnamn är nyckeln,
        # och värdet är en annan dictionary med 'ingredients' och 'instructions'.
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        # Lägger till ett recept. 'ingredients' förväntas vara en lista med ingrediensernas namn,
        # och 'instructions' en lista med steg-för-steg-instruktioner.
        self.recipes[name] = {'ingredients': ingredients, 'instructions': instructions}

    def remove_recipe(self, name):
        # Tar bort ett recept baserat på dess namn.
        if name in self.recipes:
            del self.recipes[name]

    def get_recipe(self, name):
        # Visar ingredienser och instruktioner för ett valt recept.
        if name in self.recipes:
            recipe = self.recipes[name]
            print(f"Ingredienser för {name}: {', '.join(recipe['ingredients'])}")
            print("Instruktioner:")
            for step, instruction in enumerate(recipe['instructions'], start=1):
                print(f"{step}. {instruction}")
        else:
            print("Receptet finns inte.")

    def list_recipes(self):
        # Listar alla receptnamn som finns lagrade.
        if self.recipes:
            print("Tillgängliga recept:")
            for name in self.recipes.keys():
                print(name)
        else:
            print("Inga recept tillgängliga.")
