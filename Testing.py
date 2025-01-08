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
    turtle.setworldcoordinates(0, 0, 3, 3) # an opportunity for dry code to be implemented here 

    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["pacMan","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"]
    ]
    for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan":
                    pacManX = x
                    pacManY = y
                    

    #Spawn in the pacMan turtle 
    pacMan = turtle.Turtle()
    pacMan.penup()

    pacManDirection = None # a global variable that will allow for player movement 

    """===functions to change the pacManDirection of the player==="""
    def pacManDirectionUp():
        nonlocal pacManDirection
        pacManDirection = "Up"
    def pacManDirectionRight():
        nonlocal pacManDirection
        pacManDirection = 2
    def pacManDirectionDown():
        nonlocal pacManDirection
        pacManDirection = 3
    def pacManDirectionLeft():
        nonlocal pacManDirection
        pacManDirection = 4

    def updateModel():
        #Update the maze model based on player input 
        nonlocal pacManDirection, pacManX, pacManY
        print("1"+pacManX,pacManY)
        if pacManDirection == "Up": 
            Maze[pacManX][pacManY] = "pacMan"
            #Move the player based on their input 
            Maze[pacManX][pacManY] = "Empty"
            if pacManY+1 > 3:
                window.bye()
            Maze[pacManX][pacManY+1] = "pacMan" 

    def animate():
        # 1. clear the current frame(Isn't relevant now. 1/8)
        pacMan.clear()

        # 2. update the model -- i.e. in memory state of the game via the 2d list
        updateModel()
        
        # 3. render the next frame
        for x in range(4):
            for y in range(4):
                if Maze[x][y] == "pacMan": 
                    print("2"+x,y)
                    pacMan.goto(x,y)
                    pacMan.dot(8)

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