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
    turtle.setworldcoordinates(0, 0, 4, 4)

    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["pacMan","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"],
        ["empty","empty","empty","empty"]
    ]

    #Spawn in the pacMan turtle 
    pacMan = turtle.Turtle()
    pacMan.penup()

    def movePlayer():
        nonlocal pacMan

    def animate():
        # 1. clear the current frame(Isn't relevant now.)
        pacMan.clear()

        # 2. update the model -- i.e. in memory state of the game via the 2d list
        for row in Maze:
            for column in row:
                if Maze[row][column] == "pacMan":
                    pacMan.goto([row][column])
                    pacMan.dot(8)
        # 3. re-render the next frame

        #implement player movement now

        # 4. set a timer to call this function again for the next frame
        window.ontimer(animate,1000) #hardcode some movement before looping it. 

    animate()
    #pacMan.goto(0, 2)

    window.mainloop()

main()