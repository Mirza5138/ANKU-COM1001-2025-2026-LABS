# I changed the values so it matches the shape given in the pdf file. (Yes, I took my time to find the precise values xd) You can change the length, angle and scale factor however you want and experiment with it. :P
import turtle

length = 100
angle = 40
scale = 0.6

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.up()
t.goto(0,-200) #Puts the pointer somewhere to the bottom so the shape is clearly visible.
t.down()

def drawBranch(d, a): #A pretty simple recursive function. It calls itself to draw each branch and terminates once it reaches the lower bound.
    if d > .1:
        t.forward(d)
        t.left(a)
        drawBranch(d*scale,a)
        t.right(2*a)
        drawBranch(d*scale,a)
        t.left(a)
        t.back(d)
    else:
        return

drawBranch(length,angle)

turtle.exitonclick()