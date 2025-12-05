import turtle

length = 200
depth = 3

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-2/length,0) #Puts the pointer somewhere to the left so the shape is centered.
t.down()

def drawEdge(lng): #Draws an edge of the triangle everytime it is called. By calling it three times in a row, it draws a complete triangle.
    t.forward(lng)
    t.left(120)

def triangleConstructinator(dep,lng): #A recursive function that goes back and forth between lower and higher depths.
    if dep == 0:                      #If it is hard to make sense of what it does, use a debugger to see it happen step by step.
        drawEdge(lng)
    elif 0 < dep <= depth:
        t.begin_fill()
        for j in range(3):
            triangleConstructinator(dep-1,lng)
        t.end_fill()
        t.forward(lng*(2**(dep)))
        t.left(120)
    else:
        return

triangleConstructinator(depth,length/(2**depth))

                 #This chunk of lines
t.color("white") #exist solely because I
t.right(120)     #couldn't figure out how
t.back(length/2) #to get ride of that line.
t.color("black") #So if you can figure out how,
                 #please fix it and contact me.

turtle.exitonclick()