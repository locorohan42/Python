#Rohan Abraham
#Program draws a compass rose

import turtle
def main():

    QUARTER_TURN = 90
    HALF_TURN = 180
    STANDARD_MOVE = 15
    
    #Draw circle
    turtle.hideturtle()
    turtle.circle(30)
    #Go to where south line should be
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    #Draw south line
    turtle.right(QUARTER_TURN)
    turtle.forward(100)
    #Write south
    turtle.penup()
    turtle.forward(STANDARD_MOVE)
    turtle.pendown()
    turtle.write("South")

    #Go to middle
    turtle.penup()
    turtle.right(HALF_TURN)
    turtle.forward(STANDARD_MOVE)
    turtle.pendown()
    turtle.forward(130)

    #Draw East line
    turtle.right(QUARTER_TURN)
    turtle.forward(100)
    #Write East
    turtle.penup()
    turtle.forward(STANDARD_MOVE)
    turtle.pendown()
    turtle.write("East")

    #Draw West Line
    turtle.penup()
    turtle.right(HALF_TURN)
    turtle.forward(STANDARD_MOVE)
    turtle.pendown()
    turtle.forward(230)
    #Write west
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.write("West")

    #Go to middle
    turtle.penup()
    turtle.right(HALF_TURN)
    turtle.forward(STANDARD_MOVE)
    turtle.pendown()
    turtle.forward(125)

    #Draw North Line
    turtle.left(QUARTER_TURN)
    turtle.forward(100)
    #Draw North
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.write("North")
    


main()
