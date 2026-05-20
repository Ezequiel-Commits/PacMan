"""A class that encapsulates the pellets that the PacMan will eat to gain points"""
import turtle
import sprite

class Pellet(sprite.Sprite):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 10
        self.turt = turtle.Turtle()
        self.turt.ht()
        self.turt.penup()
    
    def move(self):
        # replace the basic goTo function 
        self.turt.goto(self.x,self.y)

    def updateSelf(self):
        # self.x, self.y = turtle.position()
        # self.turt.goto(self.x,self.y)
        self.turt.pendown()
        self.turt.dot(self.size)
    

    