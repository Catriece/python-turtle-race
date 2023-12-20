from turtle import Turtle, Screen
import random


screen = Screen()
screen_width = 500
screen_height = 400

# Keyword argument instead of positional argument
screen.setup(width=screen_width, height=screen_height)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? "
                                                           "Enter a color from the rainbow: ").lower()
all_turtles = []

def turtle_race():
    space_between_racers = screen_height/len(colors)
    starting_place = (screen_height / 2 * -1) + space_between_racers / 2
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(f"{color}")
        new_turtle.penup()
        new_turtle.goto(x=((screen_width/2) - 20) * -1, y=starting_place)
        starting_place += space_between_racers
        all_turtles.append(new_turtle)


if user_bet:
    turtle_race()
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > screen_width / 2 - 20:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            race_is_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()