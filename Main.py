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
    
    """===variables and lists to enable movement==="""
    heading = None
    ghostHeading = None
    
    playerLocation = [0,0]
    playerSpeed = [10,10]
    
    ghostLocation = [-200,-200]
    ghost.goto(ghostLocation[0],ghostLocation[1])
    
    """===Setting up the PacMan environemt==="""
    def drawEnvironment():
        nonlocal drawer
        #Draw the environment quickly by using the tracer function, as
        #well as some hard-coded lines for the walls
        window.tracer(False)
        drawer.speed(0)
        #Bottom left
        drawer.goto(-150,-125)
        drawer.pendown()
        drawer.setheading(0)
        drawer.forward(50)
        drawer.goto(-150,-125)
        drawer.setheading(90)
        drawer.forward(50)
        drawer.penup()
        #Bottom right
        drawer.goto(150,-125)
        drawer.pendown()
        drawer.setheading(180)
        drawer.forward(50)
        drawer.goto(150,-125)
        drawer.setheading(90)
        drawer.forward(50)
        drawer.penup()
        #Top right
        drawer.goto(150,125)
        drawer.pendown()
        drawer.setheading(180)
        drawer.forward(50)
        drawer.goto(150,125)
        drawer.setheading(270)
        drawer.forward(50)
        drawer.penup()
        #Top left
        drawer.goto(-150,125)
        drawer.pendown()
        drawer.setheading(0)
        drawer.forward(50)
        drawer.goto(-150,125)
        drawer.setheading(270)
        drawer.forward(50)
        drawer.penup()

        window.update()
        window.tracer(True)
    
    
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
    
    def moveGhost2():
        nonlocal ghost, playerLocation
        #Move the ghost toward the player using the setheading function
        ghost.setheading(ghost.towards(playerLocation[0],playerLocation[1]))
        ghost.forward(6)
        #Update the ghosts position each time to allow the player to be caught
        ghostLocation[0],ghostLocation[1] = ghost.pos()
    
    def updateScreen():
        nonlocal ghostLocation, playerLocation, heading, dingo
        #Move the player and chaser almost simultaneously 
        movePlayer()
        moveGhost2()
        
        #Get the difference in the position of the player and the ghost
        xCoordDifference = abs(playerLocation[0] - ghostLocation[0])
        yCoordDifference = abs(playerLocation[1] - ghostLocation[1])
        
        if xCoordDifference < 5 and yCoordDifference < 5:
            #The ghost is close enough to have caught the player
            print("you've been caught!")
            answer = input("Do you want to play again? Y/N: ")
            while True:
                #Use a while loop to stop the player from moving
                if answer == "Y":
                    #Reset the player and ghost locations
                    print("Game starting again!")
                    playerLocation[0],playerLocation[1] = 0,0
                    dingo.goto(0,0)
                    heading = 0 
                    ghostLocation[0],ghostLocation[1] = -300,-300
                    ghost.goto(ghostLocation[0],ghostLocation[1])
                    #Break out of the while statement
                    break
                elif answer == "N":
                    #Close the program
                    print("Game terminating")
                    window.bye()
                    break
                else:
                    print("Please enter a valid response")
                    answer = input("Do you want to play again? Y/N: ")
        #Repeat the function every 1/10th of a second
        window.ontimer(updateScreen,100)
    
    drawEnvironment()
    print("Game starting, avoid the ghost for as long as you can")
    updateScreen() 
    
    """=== player keybinds==="""
    window.onkeypress(headingUp, key = "Up")
    window.onkeypress(headingDown, key = "Down")
    window.onkeypress(headingRight, key = "Right")
    window.onkeypress(headingLeft, key = "Left")
    window.listen()
    
    window.mainloop()

main()
