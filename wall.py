# Import some libraries for later use 
import turtle

# Create a class called "Wall"
class Wall:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.turt = turtle.Turtle()
    
    def move(self):
        # replace the basic goTo function 
        self.turt.penup()
        self.turt.goto(self.x,self.y)
        self.turt.pendown()

    def drawDot(self, dotSize):
        # replace the basic dot function 
        self.turt.dot(dotSize)
        