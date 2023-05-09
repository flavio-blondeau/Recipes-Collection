import functions
import PySimpleGUI as sg
import os


# window for adding new recipe
def new_recipe_window():
    name_label = sg.Text("Recipe name:")
    name_input = sg.InputText(tooltip="Name here", key="name")
    description_label = sg.Text("Short description:")
    description_input = sg.Multiline(tooltip="Description here", key="description", size=(45, 5))
    ingredients_label = sg.Text("Ingredients (use a comma to separate ingredients):")
    ingredients_input = sg.Multiline(tooltip="Ingredients here", key="ingredients", size=(45, 5))
    add_new_button = sg.Button("Add to collection")
    cancel_button = sg.Button("Cancel")

    window2 = sg.Window("Add new recipe",
                        layout=[
                            [name_label],
                            [name_input],
                            [description_label],
                            [description_input],
                            [ingredients_label],
                            [ingredients_input],
                            [add_new_button, cancel_button]
                        ],
                        font=('Helvetica', 16))
    while True:
        event2, values2 = window2.read()
        match event2:
            case "Add to collection":
                ingredients = values2['ingredients'].split(',')
                ingredients = [item.lower().strip() for item in ingredients]
                new_recipe = {
                    "name": values2['name'],
                    "description": values2['description'],
                    "ingredients": ingredients
                }
                if '' in new_recipe.values() or None in new_recipe.values():
                    sg.Popup("Please fill in all forms!", font=('Helvetica', 16))
                else:
                    recipes = functions.open_recipes()
                    recipes.append(new_recipe)
                    functions.store_recipes(recipes)
                    window['recipes'].update(values=[item['name'] for item in recipes])
                    break
            case "Cancel":
                break
            case sg.WIN_CLOSED:
                break

    window2.close()


def show_recipe_window(recipe_name):
    recipes = functions.open_recipes()
    recipe_index = [index for index, d in enumerate(recipes) if d['name'] == recipe_name][0]
    recipe = recipes[recipe_index]
    name_label = sg.Text(f"Recipe: {recipe['name']}")
    description_label = sg.Text(f"Description: {recipe['description']}")
    ingredients_label = sg.Text("Ingredients:")
    ingredients_box = sg.Listbox(values=recipe['ingredients'], key='ingredients', size=(30, 8))
    cancel_button = sg.Button("Cancel")

    window3 = sg.Window(f"Recipe: {recipe_name}",
                        layout=[
                            [name_label],
                            [description_label],
                            [ingredients_label],
                            [ingredients_box],
                            [cancel_button]
                        ],
                        font=('Helvetica', 16))

    while True:
        event3, values3 = window3.read()
        match event3:
            case "Cancel":
                break
            case sg.WIN_CLOSED:
                break

    window3.close()


# upload recipes file or create an empty file
if not os.path.exists("recipes.json"):
    functions.store_recipes([])

sg.theme("DarkTeal10")

# Search bar (by name or ingredient)
search_label1 = sg.Text("Search for a recipe by name...")
search_input1 = sg.InputText(tooltip="Enter recipe", key='search')
search_button1 = sg.Button("Search recipe")
search_label2 = sg.Text("...or by an ingredient:")
search_input2 = sg.InputText(tooltip="Enter ingredient", key='search_ingredient')
search_button2 = sg.Button("Search ingredient")

# List of recipes
recipes_names = [item['name'] for item in functions.open_recipes()]
list_box = sg.Listbox(values=recipes_names, key='recipes',
                      size=(40, 10), enable_events=True)

# Add new recipe
add_label = sg.Text("Add new recipe:")
add_button = sg.Button("Add")

# Show again the full list
show_button = sg.Button("Show full list")

# Exit button
exit_button = sg.Button("Exit")

window = sg.Window("Recipes Collection App",
                   layout=[
                       [search_label1],
                       [search_input1, search_button1],
                       [search_label2],
                       [search_input2, search_button2],
                       [add_label, add_button],
                       [list_box, show_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            new_recipe_window()

        case 'Search recipe':
            name = values['search'].lower().strip()
            if name == '' or name is None:
                sg.Popup("You have not typed yet!", font=('Helvetica', 16))
            else:
                recipes_list = functions.open_recipes()
                indices = []
                for i in range(len(recipes_list)):
                    recipe_name = recipes_list[i]['name'].lower()
                    if name in recipe_name:
                        indices.append(i)
                selected_recipes = [recipes_list[index] for index in indices]
                window['recipes'].update(values=[item['name'] for item in selected_recipes])
            window['search'].update(value='')

        case 'Search ingredient':
            ingredient = values['search_ingredient'].lower().strip()
            if ingredient == '' or ingredient is None:
                sg.Popup("You have not typed yet!", font=('Helvetica', 16))
            else:
                recipes_list = functions.open_recipes()
                indices = []
                for i in range(len(recipes_list)):
                    recipe_ingredients = recipes_list[i]['ingredients']
                    for ingr in recipe_ingredients:
                        if ingredient in ingr:
                            indices.append(i)
                selected_recipes = [recipes_list[index] for index in indices]
                window['recipes'].update(values=[item['name'] for item in selected_recipes])
            window['search_ingredient'].update(value='')

        case 'Show full list':
            recipes_list = functions.open_recipes()
            window['recipes'].update(values=[item['name'] for item in recipes_list])

        case 'recipes':
            recipe_name = values[event][0]
            show_recipe_window(recipe_name)

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
