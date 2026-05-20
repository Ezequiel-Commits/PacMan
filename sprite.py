"""A superclass for all sprites(pacMan, ghost, pellets, walls, etc.) in the game"""
import turtle

class Sprite:
    def __init__(self, size = 10):
        self.size = size
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.ht()
    
    def draw(self, x = 0, y = 0):
        self.turt.goto(x, y)
        self.turt.dot(self.size)

    def undraw(self):
        self.turt.clear()
    