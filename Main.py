import time
import turtle 

window  = None
WINX, WINY = 1000,1000

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
    # reset the coordinate system so that the bottom left is (0, 0) and the top right is (4, 4)
    turtle.setworldcoordinates(0, 0, 4, 4) # an opportunity for dry code to be implemented here 
    turtle.tracer(False) # Make the turtle animations faster

    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["pacMan","empty","empty","empty"],
        ["ghost","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"]
    ]
    

    #Spawn in the pacMan turtle and ghost turtles
    pacMan = turtle.Turtle()
    pacMan.penup()
    pacMan.speed(0)
    ghost = turtle.Turtle()
    ghost.penup()
    ghost.speed(0)

    pacManDirection = "none" # a global variable that will allow for player movement 

    """===functions to change the pacManDirection of the player==="""
    def pacManDirectionUp():
        nonlocal pacManDirection
        pacManDirection = "Up"
    def pacManDirectionRight():
        nonlocal pacManDirection
        pacManDirection = "Right"
    def pacManDirectionDown():
        nonlocal pacManDirection
        pacManDirection = "Down"
    def pacManDirectionLeft():
        nonlocal pacManDirection
        pacManDirection = "Left"

    """Functions to move both the player and the ghost"""
    def movePacMan(pacManX,pacManY):
        nonlocal pacManDirection
        if pacManDirection == "Up": 
            #Move the player based on their input 
            Maze[pacManX][pacManY] = "Empty"
            if pacManY+1 > 3: #pacMan is too close to a wall, so stop pacMan 
                # from moving 
                Maze[pacManX][pacManY] = "pacMan" #reassign the pacMan coordinates
                return
            Maze[pacManX][pacManY+1] = "pacMan" 
        elif pacManDirection == "Down": 
            Maze[pacManX][pacManY] = "Empty"
            if pacManY-1 < 0:
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX][pacManY-1] = "pacMan"
        elif pacManDirection == "Right": 
            Maze[pacManX][pacManY] = "Empty"
            if pacManX+1 > 3:
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX+1][pacManY] = "pacMan"
        elif pacManDirection == "Left": 
            Maze[pacManX][pacManY] = "Empty"
            if pacManX-1 < 0:
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX-1][pacManY] = "pacMan"

    def moveGhost(ghostX,ghostY,pacManX,pacManY):
        if pacManY > ghostY:
            #If the player is above the ghost
            Maze[ghostX][ghostY] = "Empty"
            if ghostY+1 > 3: 
                Maze[ghostX][ghostY] = "ghost"
                return
            Maze[ghostX][ghostY+1] = "ghost"
        pass

    def updateModel():
        #Update the maze model based on player input 
        # print("test1")
        ghostX, ghostY, pacManX, pacManY = None, None, None, None

        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan":
                    # print("test2")
                    pacManX = x
                    pacManY = y
        # Update the ghost based on the player's location
        # print("test2.5")
        # print(Maze[3][3])
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "ghost":
                    # print("test3")
                    ghostX = x
                    ghostY = y
        # xCoordDifference = pacManX - ghostX
        # yCoordDifference = pacManY - ghostY
        # if xCoordDifference == 0 and yCoordDifference == 0:
        #     # Check if the player has collided with the ghost, or vice versa 
        #     while True:
        #         print("you've been caught!")
        #         # Stop the program from freezing
        #         time.sleep(1)
        if pacManX != None and pacManY != None:
            movePacMan(pacManX,pacManY)
        #The ghost should move based on player input as well
        if ghostX != None and ghostY != None:
            moveGhost(ghostX,ghostY,pacManX,pacManY)




    def render():
        """Draw the current frame""" 
        nonlocal Maze
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan": 
                    pacMan.goto(x,y)
                    pacMan.dot(30)
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "ghost": 
                    ghost.goto(x,y)
                    ghost.dot(30)
        turtle.update()

    def animate():
        # 1. clear the current frame(Isn't relevant now. 1/8)
        pacMan.clear() 
        ghost.clear() # The ghost.turtle sprite stays

        # 2. update the model -- i.e. in memory state of the game via the 2d list
        updateModel()
        
        # 3. render the next frame
        render()

        # 4. set a timer to call this function again for the next frame
        window.ontimer(animate,1000)

    animate()

    """=== player keybinds==="""
    window.onkeypress(pacManDirectionUp, key = "Up")
    window.onkeypress(pacManDirectionDown, key = "Down")
    window.onkeypress(pacManDirectionRight, key = "Right")
    window.onkeypress(pacManDirectionLeft, key = "Left")
    window.listen()

    window.mainloop()

main()