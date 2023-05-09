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
        print('ADD', event2)
        print('ADD', values2)
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
                    sg.Popup("Please fill in all forms!")
                else:
                    recipes = functions.open_recipes()
                    recipes.append(new_recipe)
                    functions.store_recipes(recipes)
                    break
            case "Cancel":
                break
            case sg.WIN_CLOSED:
                break

    window2.close()


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
                      size=(40, 10))

# Add new recipe
add_label = sg.Text("Add new recipe:")
add_button = sg.Button("Add")

# Exit button
exit_button = sg.Button("Exit")

window = sg.Window("Recipes Collection App",
                   layout=[
                       [search_label1],
                       [search_input1, search_button1],
                       [search_label2],
                       [search_input2, search_button2],
                       [list_box, add_label, add_button],
                       [exit_button]
                   ],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == 'Add':
        new_recipe_window()
    if event == sg.WIN_CLOSED:
        break

window.close()
