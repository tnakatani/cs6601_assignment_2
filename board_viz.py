# Board visualization with ipywidgets
from ipywidgets import Button, GridBox, Layout, ButtonStyle
from IPython.display import display, clear_output
from time import sleep

def on_button_clicked(b):
    pass #print(b.x, b.y)

def get_details(name):
    if name == 'Q1':
        color = 'SpringGreen'
    elif name == 'Q2':
        color = 'tomato'
    elif name == 'q1':
        color = 'HoneyDew'
        name = ' '
    elif name == 'q2':
        color = 'MistyRose'
        name = ' '
    elif name == 'X':
        color = 'black'
    else:
        color = 'Lavender'
    style = ButtonStyle(button_color=color)
    return name, style

def create_cell(button_name='', grid_loc=None):
    layout = Layout(width='auto', height='auto')
    name, style = get_details(button_name)
    button = Button(description=name,layout = layout, style=style)
    button.x, button.y = grid_loc
    button.on_click(on_button_clicked)
    return button