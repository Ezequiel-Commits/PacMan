import turtle 

window  = None
WINX, WINY = 30,30

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

    #Definting the game using a 2d list 
    game = [
        ["pacMan","empty","empty"],
        ["empty","empty","empty"],
        ["empty","empty","empty"]
    ]

    #Spawn in the pacMan turtle 
    pacMan = turtle.Turtle()
    pacMan.penup()

    """===variables and lists to enable movement==="""
    pacManDirection = None

    pacManLocation = [0,0]
    pacManSpeed = [1,1]

    """===functions to change the direction of the player==="""
    def pacManDirectionUp():
        nonlocal pacManDirection
        pacManDirection = 1
    def pacManDirectionRight():
        nonlocal pacManDirection
        pacManDirection = 2
    def pacManDirectionDown():
        nonlocal pacManDirection
        pacManDirection = 3
    def pacManDirectionLeft():
        nonlocal pacManDirection
        pacManDirection = 4

    def movePlayer():
        pass

    def animate():
        #clear frame
        #update the model
        #render
        #run the function every 30 milliseconds
        pass

    window.mainloop()

main()