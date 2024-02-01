import mysql.connector

# Create all functions
# Calculate difficulty, used in create_recipe()
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
# Function to display recipes
def display_recipe(recipe):
    print(f"Name: {recipe[1]}")
    print(f"Cooking Time: {recipe[3]} minutes")
    print(f"Ingredients: {recipe[2]}")
    print(f"Difficulty: {recipe[4]}")
    print()

# 1. User enterts a recipe, used in main_menu()
def create_recipe(conn, cursor):
    # Prompt the user for the name of the recipe
    val_name = input("Enter the name of the recipe: ")
    val_name = val_name.capitalize()

    # Prompt the user for the cooking time and convert it to an integer
    val_cooking_time = int(input("Enter the cooking time (in minutes): "))

    # Prompt the user for ingredients and store them in a list
    val_ingredients = []
    print("Enter the ingredients (type 'done' when finished):")
    while True:
        ingredient = input("> ")
        if ingredient.lower() == 'done':
            break
        val_ingredients.append(ingredient.capitalize())
    
    # Calculate the difficulty
    val_difficulty = calc_difficulty(val_cooking_time, len(val_ingredients))

    # Add the recipe to the database
    # Convert ingredients list to a string
    ingredients_str = ', '.join(val_ingredients)
    cursor.execute(f"INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES ('{val_name}', '{ingredients_str}', {val_cooking_time}, '{val_difficulty}')")
    conn.commit()

    # Show the user the recipe they just created
    print("\nThe following recipe has been added:")
    print(f"Name: {val_name}")
    print(f"Cooking Time: {val_cooking_time} minutes")
    print(f"Ingredients: {ingredients_str}")
    print(f"Difficulty: {val_difficulty}")

# 2. User can search for a recipe, used in main_menu()
def search_recipe(conn, cursor):
    # Prompt the user for the ingredient to search for
    # Query to select all recipes from the Recipes table
    cursor.execute("SELECT * FROM Recipes")

    # Fetch all rows
    recipes = cursor.fetchall()

    # Set to store unique ingredients
    unique_ingredients = set()

    # Process each row
    for recipe in recipes:
        ingredients_list = recipe[2].split(', ')  # Split the ingredients string into a list
        unique_ingredients.update(ingredient.capitalize() for ingredient in ingredients_list)  # Add ingredients to the set

    # Convert the set to a list and sort it alphabetically
    sorted_ingredients = sorted(list(unique_ingredients))

    # Display numerated list of unique, sorted ingredients
    print("\nIngredients:")
    
    for idx, ingredient in enumerate(sorted_ingredients, 1):
        print(f"{idx}. {ingredient}")
    
    print()

    # Prompt the user for the ingredient to search for
    while True:
        try:
            idx = int(input("Enter the number of the ingredient you want to search for: ")) - 1  # convert to zero-based index
            if 0 <= idx < len(sorted_ingredients):
                ingredient_searched = sorted_ingredients[idx]  # Retrieve the ingredient
                print(f"You selected: {ingredient_searched}")
                print()
                print("\nRecipes that contain this ingredient:")
                
                recipes_with_ingredient = []
                for recipe in recipes:
                    if ingredient_searched in recipe[2]:
                        recipes_with_ingredient.append(recipe)
                        display_recipe(recipe)  # Display each recipe that contains the ingredient
                break
            else:
                print("Invalid selection. Please enter a valid number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

# 3. User can update an existing recipe, used in main_menu()
def update_recipe(conn, cursor):
    
    # Query to select all recipes from the Recipes table
    cursor.execute("SELECT * FROM Recipes")

    # Fetch all recipes
    recipes = cursor.fetchall()

    # Create list of recipe names
    recipe_list = []

    # Process each row
    for recipe in recipes:
        recipe_name = recipe[1]  # Get name of each recipe
        recipe_list.append(recipe_name)  # Add recipe name to the list
    
    recipe_list.sort()  # Sort the list alphabetically

    # Display numerated list of unique, sorted ingredients
    print("\nRecipes:")
    
    for idx, recipe in enumerate(recipe_list, 1):
        print(f"{idx}. {recipe}")
    
    print()

    # Prompt the user for the recipe to change
    while True:
        try:
            idx = int(input("Enter the number of the recipe you want to change: ")) - 1  # convert to zero-based index
            if 0 <= idx < len(recipe_list):
                recipe_chosen = recipe_list[idx]  # Retrieve the recipe name
                print(f"You selected: {recipe_chosen}")
                print()
                
                chosen_column = (input(
                """
                Choose the number of the column to update:
                1. Name
                2. Cooking Time
                3. Ingredients
                """
                ))

            # Execute function base on choice
                if chosen_column == "1":
                    val_name = input("Enter the new name of the recipe: ")
                    # identify the recipe to update, then update the name
                    cursor.execute(f"UPDATE Recipes SET name = '{val_name}' WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    # print the updated recipe
                    print()
                    print(f"Recipe name updated to '{val_name}'")
                    cursor.execute(f"SELECT * FROM Recipes WHERE name = '{val_name}'")
                    recipe = cursor.fetchone()
                    display_recipe(recipe)
                    break
                elif chosen_column == "2":
                    new_time = int(input("Enter the new cooking time of the recipe: "))
                    # identify the recipe to update, then update the name
                    cursor.execute(f"UPDATE Recipes SET cooking_time = {new_time} WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    #recalculate difficulty
                    cursor.execute(f"SELECT * FROM Recipes WHERE name = '{recipe_chosen}'")
                    recipe = cursor.fetchone()
                    num_ingredients = len(recipe[2].split(', '))
                    new_difficulty = calc_difficulty(recipe[3], num_ingredients)
                    cursor.execute(f"UPDATE Recipes SET difficulty = '{new_difficulty}' WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    # print the updated recipe
                    print()
                    print(f"Recipe time updated to '{new_time}'")
                    cursor.execute(f"SELECT * FROM Recipes WHERE name = '{recipe_chosen}'")
                    recipe = cursor.fetchone()
                    display_recipe(recipe)
                    break
                elif chosen_column == "3":
                    # Prompt the user for ingredients and store them in a list
                    val_ingredients = []
                    print("Enter the ingredients (type 'done' when finished):")
                    while True:
                        ingredient = input("> ")
                        if ingredient.lower() == 'done':
                            break
                        val_ingredients.append(ingredient.capitalize())
                    # Convert ingredients list to a string
                    ingredients_str = ', '.join(val_ingredients)
                    # identify the recipe to update, then update the ingredients
                    cursor.execute(f"UPDATE Recipes SET ingredients = '{ingredients_str}' WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    #recalculate difficulty
                    cursor.execute(f"SELECT * FROM Recipes WHERE name = '{recipe_chosen}'")
                    recipe = cursor.fetchone()
                    num_ingredients = len(recipe[2].split(', '))
                    new_difficulty = calc_difficulty(recipe[3], num_ingredients)
                    cursor.execute(f"UPDATE Recipes SET difficulty = '{new_difficulty}' WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    # print the updated recipe
                    print()
                    print(f"Recipe updated:")
                    cursor.execute(f"SELECT * FROM Recipes WHERE name = '{recipe_chosen}'")
                    recipe = cursor.fetchone()
                    display_recipe(recipe)
                    break
            else:
                print("Invalid selection. Please enter a valid number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

# 4. User can delete a recipe, used in main_menu()
def delete_recipe(conn, cursor):
    # Query to select all recipes from the Recipes table
    cursor.execute("SELECT * FROM Recipes")

    # Fetch all recipes
    recipes = cursor.fetchall()

    # Create list of recipe names
    recipe_list = []

    # Process each row
    for recipe in recipes:
        recipe_name = recipe[1]  # Get name of each recipe
        recipe_list.append(recipe_name)  # Add recipe name to the list
    
    recipe_list.sort()  # Sort the list alphabetically

    # Display numerated list of unique, sorted ingredients
    print("\nRecipes:")
    
    for idx, recipe in enumerate(recipe_list, 1):
        print(f"{idx}. {recipe}")
    
    print()

    # Prompt the user for the recipe to delete
    while True:
        try:
            idx = int(input("Enter the number of the recipe you want to delete: ")) - 1  # convert to zero-based index
            if 0 <= idx < len(recipe_list):
                recipe_chosen = recipe_list[idx]  # Retrieve the recipe name
                print(f"You selected: {recipe_chosen}")
                print()
                confirmation = input(f"Are you sure you want to delete {recipe_chosen}? (yes/no): ")
                if confirmation.lower() == "yes":
                    cursor.execute(f"DELETE FROM Recipes WHERE name = '{recipe_chosen}'")
                    conn.commit()
                    print(f"{recipe_chosen} has been deleted.")
                    break
                elif confirmation.lower() == "no":
                    print(f"{recipe_chosen} has not been deleted.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    return None
            else:
                print("Invalid selection. Please enter a valid number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None    

# Present main menu to user, user makes a choice and relevant function is executed
def main_menu(conn, cursor):
    choice = ""
    while (choice != "quit"):
        choice = input("""
        Main Menu:
        ====================================
        Pick a choice by entering a number:
        1. Create a new recipe
        2. Search for a recipe by ingredient
        3. Update an existing Recipe
        4. Delete a Recipe
        Type 'quit' to exit the program.
        Your choice: """)

        print()

# Execute function base on choice
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("USE task_database")
main_menu(conn, cursor)