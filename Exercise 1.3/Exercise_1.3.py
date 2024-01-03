recipes_list = []
ingredients_list = []
n = int(input("How many recipes would you like to add? "))

def take_recipe():
    # Prompt the user for the name of the recipe
    name = input("Enter the name of the recipe: ")

    # Prompt the user for the cooking time and convert it to an integer
    cooking_time = int(input("Enter the cooking time (in minutes): "))

    # Prompt the user for ingredients and store them in a list
    ingredients = []
    print("Enter the ingredients (type 'done' when finished):")
    while True:
        ingredient = input("> ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }

for i in range(n):
    
    # Run take_recipe and store its output
    recipe = take_recipe()

    # Iterate through the recipe's ingredients
    for ingredient in recipe['ingredients']:
        # Check if the ingredient is not already in the ingredients_list
        if ingredient not in ingredients_list:
            # Add it to the list
            ingredients_list.append(ingredient)

    # Append the recipe to the recipes_list
    recipes_list.append(recipe)

for recipe in recipes_list:
    # Determine difficulty level
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = "Easy"
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = "Medium"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = "Intermediate"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = "Hard"
    
    # Print the recipe
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {difficulty}")
    print("")

print("Ingredients List:")
for ingredient in ingredients_list:
    print(f"- {ingredient}")