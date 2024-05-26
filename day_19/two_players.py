import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cordinate = [-60, -30, 0, 30, 60, 90]
user_1_bet = screen.textinput(title="Make your bet", prompt=f"Pic a turtle color: red, orange, yellow, green ,blue, purple")
user_2_bet = screen.textinput(title="Make your bet", prompt=f"Pic a turtle color: red, orange, yellow, green ,blue, purple")

is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    tortugas = Turtle(shape='turtle')
    tortugas.penup()
    tortugas.color(colours[turtle_index])
    tortugas.setposition(x= -240, y= y_cordinate[turtle_index])
    all_turtles.append(tortugas)

if user_2_bet:
    is_race_on = True

play_again = True
while play_again:
    winning_color = ''
    while is_race_on:
        for turtle in all_turtles:

            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_1_bet:
                    print(f"Noni you WON!!!!!, the winning color is {winning_color}")
                elif winning_color == user_2_bet:
                    print(f"Noni, I WON lol!!!!!, the winning color is {winning_color}")
                else:
                    print(f"Ya'll LOST!!!! the winning color is: {winning_color}")

            random_move = random.randint(0, 10)
            turtle.forward(random_move)
    
    play_again = screen.textinput(title="Go again", prompt="Do you want to play gain? y/n: ")
    if play_again == 'n':
        play_again = False

screen.exitonclick()