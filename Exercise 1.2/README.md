# Simple Addition Script

## Overview

This project consists of a simple Python script named `add.py` that prompts the user to enter two numbers, adds them together, and prints the result. It is developed in a virtual environment to ensure consistency and manage dependencies effectively.

## Data Structures

Eeach recipe is represented as a dictionary. Here's an example of what each recipe's dictionary looks like:

```
  recipe = {
    "name": "Recipe Name",
    "cooking_time": 30,  # in minutes
    "ingredients": ["Ingredient1", "Ingredient2", ...]
}

```

This data structure is used throughout the application for creating, editing, searching, and deleting recipes. It enables efficient and intuitive handling of recipe data, ensuring a seamless user experience.

Why a Dictionary?

- Clarity and Readability: Each element in the recipe is associated with a clear, descriptive key. This makes it easy for users (and other developers) to understand what each part of the recipe represents without needing additional documentation or comments.
- Flexibility and Scalability: The dictionary structure allows for easy modification and expansion. New fields can be added to the recipe format (such as 'servings', 'nutrition facts', or 'category') without disrupting existing data or requiring major structural changes.
- Direct Access: The dictionary format allows for direct access to any part of the recipe using its key. This is particularly useful for features like editing a specific part of a recipe or displaying detailed information.

## Setup and Installation

### Virtual Environment

- If you haven't already, set up a virtual environment named `<name-of-environment>` for this project.

### Requirements File

- A `requirements.txt` file is included, which lists all the necessary Python packages.
- To install these packages, activate your virtual environment and run:
  ```
  pip install -r requirements.txt
  ```

## Running the Script

1. **Activate the Virtual Environment**:

   ```bash
   source path/to/<name-of-environment>/bin/activate  # For Unix-like systems
   path	o\<name-of-environment>\Scriptsctivate     # For Windows
   ```

2. **Run the Script**:

   ```bash
   python add.py
   ```

3. **Follow the Prompts**: Enter two numbers as prompted, and the script will display their sum.
