# Import some libraries for future refernce
import turtle 
import wall
import graph

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
        ["pacMan","empty","empty","empty"],
        ["empty","empty","wall","empty"],
        ["empty","empty","wall","empty"],
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
            Maze[pacManX][pacManY] = "empty"
            if pacManY+1 > 3 or Maze[pacManX][pacManY+1] == "wall": #pacMan is too close to a wall, so stop pacMan from moving 
                Maze[pacManX][pacManY] = "pacMan" #reassign the pacMan coordinates
                return
            Maze[pacManX][pacManY+1] = "pacMan" 
        elif pacManDirection == "Down": 

            Maze[pacManX][pacManY] = "empty"
            if pacManY-1 < 0 or Maze[pacManX][pacManY-1] == "wall":
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX][pacManY-1] = "pacMan"
        elif pacManDirection == "Right": 

            Maze[pacManX][pacManY] = "empty"
            if pacManX+1 > 3 or Maze[pacManX+1][pacManY] == "wall":
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX+1][pacManY] = "pacMan"
        elif pacManDirection == "Left": 

            Maze[pacManX][pacManY] = "empty"
            if pacManX-1 < 0 or Maze[pacManX-1][pacManY] == "wall":
                Maze[pacManX][pacManY] = "pacMan"
                return
            Maze[pacManX-1][pacManY] = "pacMan"

    """Move the ghost based on the pacMan's location"""
    def moveGhost(ghostX,ghostY,pacManX,pacManY):
        myGhostTracking = graph.Graph(4) #Unit testing

        # Not sure how this will match up with the maze 
        myGhostTracking.add_vertex_data(0, 'A')
        myGhostTracking.add_vertex_data(1, 'B')
        myGhostTracking.add_vertex_data(2, 'C')
        myGhostTracking.add_vertex_data(3, 'D')

        myGhostTracking.add_edge(0, 1, 1)  # A - B, weight 1
        myGhostTracking.add_edge(0, 2, 2)  # A - C, weight 2
        myGhostTracking.add_edge(0, 3, 3)  # A - D, weight 3

        distances = myGhostTracking.dijkstra('A')
        for i, a in enumerate(distances): #I don't completely understand this 
            print(f"Shortest distance from A to {myGhostTracking.vertex_data[i]}: {a}")

    """Update the maze model based on player input """
    def updateModel():
        ghostX, ghostY, pacManX, pacManY = None, None, None, None

        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan":
                    # print("test2")
                    pacManX = x
                    pacManY = y
                # else: 
                #     print("You died")
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "ghost":
                    # print(x,y)
                    ghostX = x
                    ghostY = y
        
        # If the pacMan has collided with a ghost, one of their coordinates should be wiped, and 
        # the move function should not run for that character. 
        if pacManX != None and pacManY != None:
            movePacMan(pacManX,pacManY)
        
        if ghostX != None and ghostY != None and pacManX != None and pacManY != None:
            moveGhost(ghostX,ghostY,pacManX,pacManY)

    """Draw the current frame""" 
    def render():
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

    """animate the screen using a model-view paradigm """
    def animate():

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

    """A function to print out the maze layout"""
    def printMaze():
        print(Maze)


    """=== player keybinds==="""
    window.onkeypress(pacManDirectionUp, key = "Up")
    window.onkeypress(pacManDirectionDown, key = "Down")
    window.onkeypress(pacManDirectionRight, key = "Right")
    window.onkeypress(pacManDirectionLeft, key = "Left")
    window.onkeypress(printMaze, key = "t")
    # Listen for player input 
    window.listen()

    window.mainloop()

main()