import pickle

# Define function that displays the recipe
def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")

# Define function that enables the user to search for a recipe
def search_ingredient(data):
    for i, ingredient in enumerate(data['all_ingredients'], 1):  # Start counting from 1
        print(f"{i}. {ingredient}")

    while True:
        try:
            idx = int(input("Enter the number of the ingredient you want to search for: ")) - 1  # convert to zero-based index
            if 0 <= idx < len(data['all_ingredients']):
                ingredient_searched = data['all_ingredients'][idx]  # Retrieve the ingredient
                print(f"You selected: {ingredient_searched}")
                print("Recipes that contain this ingredient:")
                
                recipes_with_ingredient = []
                for recipe in data['recipes_list']:
                    if ingredient_searched in recipe['ingredients']:
                        recipes_with_ingredient.append(recipe)
                        display_recipe(recipe)  # Display each recipe that contains the ingredient
                break
            else:
                print("Invalid selection. Please enter a valid number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

# Main code that prompts user to open a file and search for recipes with an ingredient
filename = input("Enter the name of the file you want to open: ")

try:
    # Try to open the file and load the data
    with open(filename, 'rb') as file:
        data = pickle.load(file)

except FileNotFoundError:
    # Handle case where the file doesn't exist
    print(f"No such file with the name {filename}.")

except Exception as e:
    # Handle other exceptions that may occur
    print(f"An error occurred: {e}.")

else:
    # If no exceptions occurred, prompt the user to search for a recipe
    print("File loaded successfully.")
    search_ingredient(data)