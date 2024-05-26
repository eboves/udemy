from turtle import Turtle, Screen
import random

screen = Screen()

"""
thi is a game of drawing something in the screen


# def move_forward():
#     titi.forward(10)

# def move_backward():
#     titi.backward(10)

# def clock_wise():
#     titi.right(10)
#     # or heading_new = titi.heading() + 10 ==> titi.setheading(heading_new)

# def counter_clock_wise():
#     titi.left(-10)

# def clear_all():
#     titi.penup()
#     titi.clear()
#     titi.setposition(0,0)
#     titi.seth(0) # or titi.home()
#     titi.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="b", fun=move_backward)
# screen.onkey(key="d", fun=clock_wise)
# screen.onkey(key="a", fun=counter_clock_wise)
# screen.onkey(key="c", fun=clear_all)

"""
screen.setup(width=500, height=400)

is_race_on: False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter you color: ")


colours = ["red", "orange", "yellow", "green", "blue", "purple"]

y_coordinates = [-60, -30, 0, 30, 60, 90]

all_turtles = []

for turtle_index in range(0, 6):
    tortugas = Turtle(shape="turtle")
    tortugas.penup()
    tortugas.color(colours[turtle_index])
    tortugas.setposition(x=-240, y=y_coordinates[turtle_index])
    all_turtles.append(tortugas)
# this if statement check if the user has make a bet and if so chance the race to TRUE
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You WON!!! the wining turtle color is: {winning_color}")
            else:
                print(f"You LOST!!! the wining turtle color is: {winning_color}")

        x_cordinate = random.randint(0, 10)
        turtle.forward(x_cordinate)





screen.exitonclick()