# Import some libraries for future refernce
import turtle 
import pellet
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
        ["pacMan","pellet","pellet","pellet"],
        ["empty","empty","wall","empty"],
        ["empty","empty","wall","pellet"],
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
    def moveGhost(ghostX,ghostY,pacManX,pacManY): # Do I implement Dijkstra's algorithm here? 
        # Create a graph of size 4
        myGhostGraph = graph.Graph(4) 
        # To make sure this works, I'll need an end with multiple paths to it, no? 
        # Say I get the shortest path to the pacMan. How can I get the ghost to follow that path? 

        # Create vertexes in a graph that represent different tiles on the screen
        myGhostGraph.add_vertex_data(0, 'A')
        myGhostGraph.add_vertex_data(1, 'B')
        myGhostGraph.add_vertex_data(2, 'C')
        myGhostGraph.add_vertex_data(3, 'D')

        # Define edges that serve as the "time" between two vertexes.
        myGhostGraph.add_edge(0, 1, 1)  # A - B, weight 1
        myGhostGraph.add_edge(0, 2, 2)  # A - C, weight 2
        myGhostGraph.add_edge(0, 3, 3)  # A - D, weight 3

        #Run Dijkstra's algorithm on the graph defined above and store it in a variable
        distances = myGhostGraph.dijkstra(start_vertex_data = 'A')
        # I don't completely understand this for loop usage
        for i, a in enumerate(distances): 
            # I've somehow gotten the 
            print(f"Shortest distance from A to {myGhostGraph.vertex_data[i]}: {a}")
            

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
        
        # if ghostX != None and ghostY != None and pacManX != None and pacManY != None:
        #     moveGhost(ghostX,ghostY,pacManX,pacManY)

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
                    newWall.updateSelf(20)
        # render the pellets
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pellet": 
                    newPellet = pellet.Pellet(x,y)
                    newPellet.move()
                    newPellet.updateSelf(10)
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