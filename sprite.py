"""A superclass for all sprites(pacMan, ghost, pellets, walls, etc.) in the game"""
import turtle

class Sprite:
    def __init__(self, size = 10):
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.ht()
    
    def draw(self, x = 0, y = 0):
        self.turtle.goto(x, y)
        self.turtle.dot(self.size)

    def undraw(self):
        self.turtle.clear()
    