"""A class to encapsulate the PacMan controlled by the player"""
import turtle
import sprite

class PacMan(sprite.Sprite):
    def __init__(self, size = 20, pencolour = "yellow"):
        # Use the superClass constructor, with some changes.
        sprite.Sprite.__init__(self, size)
        self.turt.pencolor(pencolour)
        self.x = self.turt.xcor()
        self.y = self.turt.ycor()
    
    def updateSelf(self, x, y):
        sprite.Sprite.draw(x, y)