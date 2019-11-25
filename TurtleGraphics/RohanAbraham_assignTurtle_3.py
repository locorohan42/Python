#Rohan Abraham
#Program draws a star pattern

import turtle
def main():

    NUM_LINES = 8
    LINE_LENGTH = 200
    ANGLE = 135
    START_X = -100
    START_Y = 0
    turtle.goto(START_X, START_Y)
    turtle.hideturtle()

    #For loop that does all the work of drawing the shape
    for x in range(NUM_LINES):
        turtle.forward(LINE_LENGTH)
        turtle.left(ANGLE)

main()
