import turtle 
import random

window  = None
WINX, WINY = 400, 350

def main():
    def setupWin():
        global window
        # making turtle object
        window = turtle.Screen()
        # set screen size
        window.setup(WINX,WINY)
        # set background color
        window.bgcolor("white")
    
    setupWin()
    
    """===spawn three turtles in and get rid of their pens==="""
    ghost = turtle.Turtle()
    ghost.penup()
    dingo = turtle.Turtle()
    dingo.penup()
    drawer = turtle.Turtle()
    drawer.penup()
    drawer.hideturtle()
    
    heading = None

    playerLocation = [0,0]
    playerSpeed = [10,10]
    
    """===Create a list of lists to represent the game and allow for walls==="""
    def createWallList(xAxisBlocks, yAxisBlocks):
        #Create an empty table to receive the walls from the for loop
        wallList = []
        xBlocks = 0
        yBlocks = 0
        for i in range(xAxisBlocks+1):
            #For the number of "blocks" given, add an element to represent 
            #a block of the screen 
            wallList.append([xBlocks,yBlocks])
            xBlocks += 1
        print(wallList)
   
    createWallList(10,2)

    """===functions to change the heading of the player==="""
    def headingUp():
        nonlocal heading
        heading = 1
    def headingRight():
        nonlocal heading
        heading = 2
    def headingDown():
        nonlocal heading
        heading = 3
    def headingLeft():
        nonlocal heading
        heading = 4
    
    def movePlayer():
        #The main function to move the player, making use of the 
        #heading variable
        nonlocal heading, dingo
        if heading == 0:
            pass
            #stop moving until another input is pressed
        elif heading == 1:
            #Move up
            playerLocation[1] += playerSpeed[1]
            dingo.goto(playerLocation[0],playerLocation[1]) #0 represents the x-coord, while 1 represents the y-coord
            if playerLocation[1] >= 155:
                #If you're close to a wall, stop moving
                heading = 0  
        elif heading == 2:
            #Move right
            playerLocation[0] += playerSpeed[0]
            dingo.goto(playerLocation[0],playerLocation[1])
            if playerLocation[0] >= 180:
                heading = 0
        elif heading == 3:
            #Move down
            playerLocation[1] -= playerSpeed[1]
            dingo.goto(playerLocation[0],playerLocation[1])
            if playerLocation[1] <= -155:
                heading = 0
        elif heading == 4:
            #Move left
            playerLocation[0] -= playerSpeed[0]
            dingo.goto(playerLocation[0],playerLocation[1])
            if playerLocation[0] <= -180:
                heading = 0

    """===Setting up the PacMan environemt==="""
    def drawEnvironment():
        nonlocal drawer
        #Draw the environment quickly by using the tracer function, as
        #well as some hard-coded lines for the walls
        window.tracer(False)
        drawer.speed(0)
        #Bottom left
        drawer.goto(-50,-25)
        drawer.pendown()
        drawer.setheading(0)
        drawer.forward(100)
        drawer.penup()
        window.update()
        window.tracer(True)

    drawEnvironment()

    """=== player keybinds==="""
    window.onkeypress(headingUp, key = "Up")
    window.onkeypress(headingDown, key = "Down")
    window.onkeypress(headingRight, key = "Right")
    window.onkeypress(headingLeft, key = "Left")
    window.listen()

    window.mainloop()

main()