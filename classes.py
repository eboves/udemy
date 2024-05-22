# from tkinter import W
# from turtle import Turtle, Screen

# nini = Turtle()
# nini.shape('turtle')
# nini.color("coral")
# nini.forward(100)

# print(nini)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['Pokemon Name', 'Type']
table.add_rows(
    [
        ['Pikachu', 'Electric'],
        ['Squirtle', 'Water'],
        ['Charmander', 'Fire'],
    ]
)
table.align['Pokemon Name'] = 'l'
table.align['Type'] = 'l'
print(table)