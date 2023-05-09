import json


def open_recipes():
    with open('recipes.json', 'r') as f:
        recipes_file = json.load(f)
        return recipes_file


def store_recipes(new_recipes):
    with open('recipes.json', 'w') as f:
        json.dump(new_recipes, f)
