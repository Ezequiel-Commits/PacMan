"""A class that encapsulates the pellets that the PacMan will eat to gain points"""
import turtle

class Pellet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.turt = turtle.Turtle()
        self.turt.ht()
    
    def move(self):
        # replace the basic goTo function 
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()

    def drawDot(self, dotSize):
        # replace the basic dot function 
        self.turt.dot(dotSize)