class Recipe(object):
    all_ingredients = []
    def __init__(self, name, cooking_time = None):
        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = []
        self.difficulty = None
    
    def set_name(self, name):
        self.name = int(input("Enter the name of the recipe: "))
    
    def set_time(self, cooking_time):
        self.cooking_time = int(input("Enter the cooking time: "))
    
    def get_name(self):
        output = str(self.name) # do I need to convert to string?
        return output
    
    def get_time(self):
        output = str(self.cooking_time)
        return output
    
    def add_ingredients(self, *args):
        for ingredient in args:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
    
    def get_ingredients(self):
        output = str(self.ingredients)
        return output
    
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty
    
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def __str__(self):
        self.calculate_difficulty()
        ingredients_str = ", ".join(self.ingredients)
        output = "\nName: " + str(self.name) + "\nCooking Time: " + str(self.cooking_time) + "\nIngredients: " + ingredients_str + "\nDifficulty: " + str(self.difficulty) + "\n"
        return output
    
    def recipe_search(data, search_term):
        found = False
        print("Recipe(s) with " + search_term + " as an ingredient: ")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                found = True
        if not found: 
            print("No recipes found.")
    
tea = Recipe("Tea")
tea.cooking_time = 5
tea.add_ingredients("tea leaves", "water", "sugar")
print(tea)
    
coffee = Recipe("Coffee")
coffee.cooking_time = 5
coffee.add_ingredients("coffee powder", "water", "sugar")
print(coffee)

cake = Recipe("Cake")
cake.cooking_time = 50
cake.add_ingredients("flour", "eggs", "sugar", "baking powder", "vanilla essence", "milk")
print(cake)

Recipe.recipe_search([tea, coffee, cake], "water")

Recipe.recipe_search([tea, coffee, cake], "sugar")

Recipe.recipe_search([tea, coffee, cake], "bananas")


