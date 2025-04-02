# A superclass for all sprites(pacMan, ghost, pellets, walls, etc.) in the game

class sprite:
    def __init__(self, x, y, size = 10):
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        pass

    def undraw(self):
        pass

    def drawBoundingCircle(self):
        pass
    