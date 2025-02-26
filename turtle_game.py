from turtle import Turtle,Screen
import random
is_game = False
screen = Screen()
screen.setup(500,400)
user_choice = screen.textinput("make your bet","which turtle win the race? enter a color: ")
color = ['red','blue','green','yellow','purple','orange']
y_position = [-70,-40,-10,20,50,80]
all_turtle = []
for i in range(6):
    tr = Turtle("turtle")
    tr.penup()
    tr.goto(-230,y_position[i])
    tr.color(color[i])
    all_turtle.append(tr)
if user_choice:
    is_game = True
while is_game:

    for tim in all_turtle:
        if tim.xcor()>230:
            winnning_color = tim.pencolor()
            if winnning_color == user_choice:
                print(f"you have win! the winning color is {winnning_color}")
                is_game = False
            else:
                print(f"sorry winning color is {winnning_color}")
                is_game = False
        random_distance = random.randint(0,10)
        tim.forward(random_distance)

screen.exitonclick()
