from turtle import Turtle, Screen
import random

# tim = Turtle(shape) #required for Etch-A-Sketch App
screen = Screen()

# functions for Etch-A-Sketch App
def move_forwards():
    new_turtle.forward(10)

def move_backwards():
    new_turtle.backward(10)

def turn_left():
    new_heading = new_turtle.heading() + 10  #to change the angle to left by 10 degrees
    new_turtle.setheading(new_heading)

def turn_right():
    new_heading = new_turtle.heading() - 10  # to change the angle to right by 10 degrees
    new_turtle.setheading(new_heading)

def clear():
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()  # to bring turtle back to coordinate (0,0)
    new_turtle.pendown()

# Etch-A-Sketch App code
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")


screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet" , prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if(user_bet):
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False  #to end the while loop
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
