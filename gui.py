import functions
import PySimpleGUI as sg
import os


def new_recipe_window():
    label = sg.Text("New window")
    window2 = sg.Window("Add new recipe",
                        layout=[
                            [label]
                        ],
                        font=('Helvetica', 16))
    while True:
        event2, values2 = window2.read()
        print('ADD', event2)
        print('ADD', values2)
        if event2 == sg.WIN_CLOSED:
            break


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
