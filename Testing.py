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
    turtle.tracer(False) # Make the turtle animations faster

    '''Definting the game using a 2d list'''
    Maze = [
        #4 by 4 list to start
        ["pacMan","pellet","pellet","pellet"],
        ["empty","empty","wall","empty"],
        ["empty","empty","wall","pellet"],
        ["ghost","empty","empty","empty"]
    ]

    window.mainloop()

main()