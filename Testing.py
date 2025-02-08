# Import some libraries for future refernce
import turtle 
import wall

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
    turtle.setworldcoordinates(0, 0, 4, 4)
    turtle.tracer(False) # Make the turtle animations faster


    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["pacMan","empty","empty","wall"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["ghost","empty","empty","empty"]
    ]
    

    #Spawn in the pacMan turtle and ghost turtles, along with doing some customization for both 
    pacMan = turtle.Turtle()
    pacMan.penup()
    pacMan.pencolor("yellow")
    pacMan.ht()

    ghost = turtle.Turtle()
    ghost.penup()
    ghost.pencolor("blue")
    ghost.ht()

    pacManDirection = "none" # a global variable that will allow for player movement 


    """===functions to change the direction of the player==="""
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
        """Move the ghost based on the pacMan's location"""
        if pacManY > ghostY:
            #If the player is above the ghost...
            Maze[ghostX][ghostY] = "Empty"
            if ghostY+1 > 3: 
                Maze[ghostX][ghostY] = "ghost"
                return
            else: #Do I need an else statement here?
                Maze[ghostX][ghostY+1] = "ghost"
        elif pacManY < ghostY:
            Maze[ghostX][ghostY] = "Empty"
            if ghostY-1 < 0: 
                Maze[ghostX][ghostY] = "ghost"
                return
            Maze[ghostX][ghostY-1] = "ghost"
        elif pacManX > ghostX:
            Maze[ghostX][ghostY] = "Empty"
            if ghostX+1 > 3: 
                Maze[ghostX][ghostY] = "ghost"
                return
            else: 
                Maze[ghostX+1][ghostY] = "ghost"
        elif pacManX < ghostX:
            Maze[ghostX][ghostY] = "Empty"
            if ghostX-1 < 0: 
                Maze[ghostX][ghostY] = "ghost"
                return
            Maze[ghostX-1][ghostY] = "ghost"


    def updateModel():
        """Update the maze model based on player input """
        ghostX, ghostY, pacManX, pacManY = None, None, None, None

        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan":
                    # print("test2")
                    pacManX = x
                    pacManY = y
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "ghost":
                    print(x,y)
                    ghostX = x
                    ghostY = y
        
        # If the pacMan has collided with a ghost, one of their coordinates should be wiped, and 
        # the move function should not run for that character. 
        if pacManX != None and pacManY != None:
            movePacMan(pacManX,pacManY)
        
        if ghostX != None and ghostY != None and pacManX != None and pacManY != None:
            moveGhost(ghostX,ghostY,pacManX,pacManY)

    def render():
        """Draw the current frame""" 
        nonlocal Maze
        # render pacMan
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan": 
                    pacMan.goto(x,y)
                    pacMan.dot(30)
        # render the ghost
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "ghost": 
                    ghost.goto(x,y)
                    ghost.dot(30)
        # render the walls
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "wall":
                    newWall = wall.Wall(x,y)
                    newWall.move()
                    newWall.drawDot(20)
        turtle.update()

    def animate():
        """animate the screen"""

        # 1. clear the current frame
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

    # Listen for player input 
    window.listen()

    window.mainloop()

main()