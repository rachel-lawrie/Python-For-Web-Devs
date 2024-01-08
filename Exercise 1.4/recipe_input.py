import pickle

# Open an existing file if applicable and set up functions to be called later

# Prompt user to enter file name
filename = input("Enter the file name: ")

# Initialize the variables
recipes_list = []
all_ingredients = []

try:
    # Try to open the file and load the data
    with open(filename, 'rb') as file:
        data = pickle.load(file)

except FileNotFoundError:
    # Handle case where the file doesn't exist
    print(f"No such file with the name {filename}. Creating a new data structure.")
    data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

except Exception as e:
    # Handle other exceptions that may occur
    print(f"An error occurred: {e}. Creating a new data structure.")
    data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

else:
    # If no exceptions occurred, close the file stream
    print("File loaded successfully.")

finally:
    # Extract the values into two separate lists
    recipes_list = data.get('recipes_list', [])
    all_ingredients = data.get('all_ingredients', [])
    print("recipes_list and all_ingredients populated.")

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"
    return difficulty

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
    
    # Calculate the difficulty
    difficulty = calc_difficulty(cooking_time, len(ingredients))

    return {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }

# Prompt user to enter additional recipes
n = int(input("How many recipes would you like to add? "))

for i in range(n):
    
    # Run take_recipe and store its output
    recipe = take_recipe()

    # Iterate through the recipe's ingredients
    for ingredient in recipe['ingredients']:
        # Check if the ingredient is not already in the ingredients_list
        if ingredient not in all_ingredients:
            # Add it to the list
            all_ingredients.append(ingredient)

    # Append the recipe to the recipes_list
    recipes_list.append(recipe)

# append new recipes and ingredients to the existing lists
data['recipes_list'] = recipes_list
data['all_ingredients'] = list(set(all_ingredients))

# print the recipes and ingedients
for recipe in recipes_list:
    
    # Sort the recipes in alphabetical order
    recipes_list = sorted(recipes_list, key=lambda x: x['name'])
    
    # Print the recipe
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")
    print()

print("Ingredients List:")
for ingredient in all_ingredients:
    print(f"- {ingredient}")

# Write the updated data back to the file
try:
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f"Updated data has been saved to {filename}.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")