
#emo kid revisted
"""
The small circles are drawn by the circle
command.
"""

from turtle import *

def yin(radius, color1, color2): #the main function takes in 3 arguments 
    width(3)
    color("blue", color1) #This color is the pencolor for the yin sign
    begin_fill() #this is a built in function from python what iyt does is draw 
    circle(radius/2., 180) #this is the small circle the fill function draws first but doesn't finish it as the radius expends and becomes bigger
    circle(radius, 180) #this line is for the bigger radius
    left(180) #obvisouly this is turning
    circle(-radius/2., 180) #this is drawing the smaller cilr in reverse
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)#the circle function draws a circle
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "white") #this is the yin and it has a black patch with a white cirle
    yin(200, "white", "black") #this is the lower yin has white patch and black circle
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
