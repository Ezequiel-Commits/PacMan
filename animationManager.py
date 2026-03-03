"""An animation Manager that will handle all animation that occures within the game"""

class animationManager:
    def __init__(self, Maze = [], rows = 4, columns = 4):
        self.rows = rows
        self.columns = columns
        # The Maze will serve as a spriteList itself
        self.Maze = Maze

    def createMaze(self):
        # Create a fleshed-out maze using the class variable
        for number1 in range(self.rows):
            # For each row...
            for number2 in range(self.columns):
                # and for each column, add an element to the list
                pass

    def updateScreen(self):
        # render all sprites in the game 
        self.Maze
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
                    # Encapsulate the pellets in a list to make deleting them easier
                    pelletList = []
                    newPellet = pellet.Pellet(x,y)
                    pelletList.append[newPellet]
                    newPellet.move()
                    newPellet.updateSelf(10)
        turtle.update()
