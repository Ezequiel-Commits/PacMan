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
    '''Proshanto's code'''
    # reset the coordinate system so that the bottom left is (0, 0) and the top right is (4, 4)
    turtle.setworldcoordinates(0, 0, 4, 4)

    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["pacMan","empty","empty","empty"]
    ]

    #Spawn in the pacMan turtle 
    pacMan = turtle.Turtle()
    pacMan.penup()

    """===variables and lists to enable movement==="""
    pacManDirection = None
    
    def goingUp():
        nonlocal pacManDirection
        pacManDirection = "up"
    def goingDown():
        nonlocal pacManDirection
        pacManDirection = "down"

    #start in the bottom left corner 
    pacManLocation = [0,0] 

    def movePlayer():
        nonlocal pacMan, pacManDirection
        xcoord = 0
        ycoord = -30
        if pacManDirection == "up":
            #Some counterintuitive code here; shouldn't the coordinates connect to the maze 2d list? 
            """
            ycoord += 20
            pacMan.goto(xcoord,ycoord)
            pacManLocation[0] -= 1
            print(pacManLocation[0])
            Maze[pacManLocation[0]+1][pacManLocation[1]]="empty" 
            Maze[pacManLocation[0]][pacManLocation[1]]="pacman" 
            """
            #print(Maze)
        elif pacManDirection == "down":
            pass


    def animate():
        # 1. clear the current frame(Isn't relevant now.)
        pacMan.clear()

        # 2. update the model -- i.e. in memory state of the game via the 2d list
        if pacManDirection == "up":
            Maze[pacManLocation[0]][pacManLocation[1]] = "empty"
            Maze[pacManLocation[0]][pacManLocation[1]] = "pacMan"
        # 3. re-render the next frame

        #implement player movement now

        # 4. set a timer to call this function again for the next frame
        window.ontimer(animate,1000) #hardcode some movement before looping it. 

    #animate()
    pacMan.goto(50, 50)

    """=== player keybinds==="""
    window.onkeypress(goingUp, key = "Up")
    window.onkeypress(goingDown, key = "Down")
    window.listen()

    window.mainloop()

main()
