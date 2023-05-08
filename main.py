import json
import os


def open_recipes():
    with open('recipes.json', 'r') as f:
        recipes_file = json.load(f)
        return recipes_file


def store_recipes(new_recipes):
    with open('recipes.json', 'w') as f:
        json.dump(new_recipes, f)


# upload recipes file or create an empty file
if not os.path.exists("recipes.json"):
    store_recipes([])

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
            recipes = open_recipes()
            recipes.append(new_recipe)
            store_recipes(recipes)

        case "search":
            pass
        case "show":
            recipes = open_recipes()
            for i, item in enumerate(recipes):
                print(f"{i}) {item['name']}")
        case "exit":
            print("Goodbye!")
            break
