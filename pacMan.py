"""A class to encapsulate the PacMan controlled by the player"""
import turtle
import sprite

class PacMan(sprite.Sprite):
    def __init__(self, size = 20):
        # Use the superClass constructor, with one small change
        sprite.Sprite.__init__(self, size)
        self.turtle.pencolor("yellow")

    
    def updateSelf(self, x, y):
        sprite.Sprite.draw(x, y)