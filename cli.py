import json
import os
import functions

# upload recipes file or create an empty file
if not os.path.exists("recipes.json"):
    functions.store_recipes([])

print("Welcome to the Recipes Collection App!")

while True:
    user_action = input("Type add, search, show or exit: ")
    user_action = user_action.lower().strip()

    match user_action:
        case "add":
            print("Add a new recipe")
            # user inserts all variables needed
            name = input("Write a name for the recipe: ")
            description = input("Write a description for the recipe: ")
            ingredients = []
            while True:
                ingr = input("Insert an ingredient or type end to exit: ")
                ingr = ingr.lower().strip()
                if ingr == 'end':
                    break
                else:
                    ingredients.append(ingr)

            # put variables into json file
            new_recipe = {"name": name, "description": description, "ingredients": ingredients}
            recipes = functions.open_recipes()
            recipes.append(new_recipe)
            functions.store_recipes(recipes)

        case "search":
            user_search = input("Want to search by name (n) or ingredients (i)? ")
            user_search = user_search.lower().strip()
            recipes = functions.open_recipes()
            match user_search:
                case 'n':
                    name = input("Type the name (or part of): ")
                    name = name.strip()
                    for i in range(len(recipes)):
                        recipe_name = recipes[i]['name']
                        if name in recipe_name:
                            print(f"Recipe nr {i+1}: {recipe_name}")
                case 'i':
                    ingr = input("Type an ingredient: ")
                    ingr = ingr.strip()
                    for i in range(len(recipes)):
                        recipe_ingredients = recipes[i]['ingredients']
                        for item in recipe_ingredients:
                            if ingr in item:
                                print(f"The ingredient {ingr} is in recipe nr {i+1} ")

        case "show":
            recipes = functions.open_recipes()
            for i, item in enumerate(recipes):
                print(f"{i+1}) {item['name']}")

        case "exit":
            print("Goodbye!")
            break
