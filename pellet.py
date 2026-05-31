"""A class that encapsulates the pellets that the PacMan will eat to gain points"""
import turtle
import sprite

class Pellet(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self, size = 10)
        self.x = x
        self.y = y
        
    
    def move(self):
        # replace the basic goTo function 
        self.turt.goto(self.x,self.y)

    def updateSelf(self):
        # self.x, self.y = turtle.position()
        # self.turt.goto(self.x,self.y)
        self.turt.pendown()
        self.turt.dot(self.size)
    

    