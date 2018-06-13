#A program that draws a polygons in two different colours
#Mholi Mncube
#23/05/2014
def polygon():
    import turtle
    a=turtle.numinput("Enter polygon sides: ","Number of Sides")
    b=turtle.numinput("Enter polygon size: ","Size of Polygon")
    c=turtle.numinput("Enter number of polygons:","Number of Polygons")
    d=turtle.textinput("Enter color: ","Colour1")
    e=turtle.textinput("Enter color: ","Colour2")
    turtle.speed(0)
    for j in range(int(c)):
        turtle.right(90)
        for i in range(int(a)):
            turtle.pencolor(d) 
            turtle.forward(int(b))
            turtle.right(int(360/a))
        if j==int((int(c)/2)):break
    turtle.right(45)
    for k in range(int(c)):
        for i in range(int(a)):
            turtle.pencolor(e)
            turtle.forward(int(b))
            turtle.right(int(360/a))
        turtle.right(90)
        if k==int((int(c)/2)): break
    turtle.home()
    turtle.exitonclick()
polygon()