#Rohan Abraham
#This program just draws two boxes that are connected with lines

import turtle
def main():
    STANDARD_MOVE = 100
    DOUBLE_MOVE = 200
    CONNECT_LENGTH_MOVE = 142
    DOUBLE_CONNECT_LENGTH_MOVE = 284
    
    STANDARD_ROTATE = 90
    HALF_ROTATE = 45
    DOUBLE_ROTATE = 180
    HARD_ROTATE = 135

    START_X = -100
    START_Y = 0

    #Setup
    turtle.hideturtle()
    turtle.goto(START_X, START_Y)
    turtle.speed(7)

    #First square
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)

    #Second square
    turtle.right(DOUBLE_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    turtle.left(STANDARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    
    #Middle line that intersects both squares
    turtle.right(HALF_ROTATE)
    turtle.forward(CONNECT_LENGTH_MOVE)
    turtle.right(DOUBLE_ROTATE)
    turtle.forward(DOUBLE_CONNECT_LENGTH_MOVE)

    #Draw Bottom intersecting line
    #Move it
    turtle.right(HARD_ROTATE)
    turtle.forward(STANDARD_MOVE)
    #Draw it once its in position
    turtle.right(HALF_ROTATE)
    turtle.forward(CONNECT_LENGTH_MOVE)

    #Draw Bottom intersecting line
    #Move it
    turtle.right(HARD_ROTATE)
    turtle.forward(DOUBLE_MOVE)
    #Draw it
    turtle.left(HARD_ROTATE)
    turtle.forward(CONNECT_LENGTH_MOVE)
    
main()
    
