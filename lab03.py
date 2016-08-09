import turtle
import math

def drawInitialsJL(t, width, height):
    '''draws the letters J and L in proportion to length'''
    #doesn't use height, goes in proprtionate to length
    #sorry added height parameter bc it wanted us to
    length = width;
    #draws the letter J
    t.color("red")
    t.setheading(0)
    t.down()
    t.left(270)
    t.forward(length/8)
    t.circle(length/4, 180)
    t.forward(3*length/4)
    t.left(90)
    t.forward(length/2)
    t.backward(length)
    #spaces the initials
    t.up()
    t.backward(length/10)
    t.down()
    #draws the letter L
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length/2)
    t.up()

def drawInitialsRK(t, width, height):
    '''draws the letters R and K in proportion to width and height'''
    t.forward(height/10) #creates space from Jef
    t.down() #puts down pen 
    t.color("green")
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width/4)
    t.circle(-width/2, 180) #creates semi circle in R, after movement away
    t.forward(width/4)
    t.left(135)
    rLeg = math.sqrt(2) # used to find length of leg for R and K, used later
    t.forward(width*rLeg)
    t.left(45)
    t.up()
    t.forward(height/10)
    t.down()
    t.left(90)
    t.forward(height)
    t.left(180)
    t.forward(height / 2)
    t.left(45)
    t.forward(width*rLeg) # reusing Rleg 
    t.right(180)
    t.forward(width*rLeg)
    t.right(90)
    t.forward(width*rLeg)

def go():
    '''this function invokes the two initial functions ''' 
    test(200)
    test(112)
    test(82)

def test(length):
    turtle.clear()
    turtle.up()
    turtle.goto(-300, 0)
    drawInitialsJL(turtle, length, length)
    drawInitialsRK(turtle, length/2, length)

turtle = turtle.Turtle()
turtle.shape("turtle")
go()
