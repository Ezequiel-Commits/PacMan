"""A manager to check for collisions between pacMan and pellets each time the screen is updated."""
import math
import pacMan
import pellet

class CollisionManager:
    def __init__(self, spriteList):
        self.spriteList = spriteList
        print(self.spriteList)
    
    def checkCollisions(self):
        
        # Use bounding circles to check if one sprite has collided with another
        for sprite1 in self.spriteList:
            for sprite2 in self.spriteList: #Two for loops to compare a pair of sprites
                if sprite1 != sprite2: #Avoid comparing the same sprites to each other
                    # Something's going on here as I change the world coordinates, though the sizes of each sprite remain quite large.  
                    distanceBetweenSprites = math.dist([sprite1.x, sprite1.y],[sprite2.x, sprite2.y])
                    if distanceBetweenSprites*250 <= sprite1.size + sprite2.size:
                        # If the distance between two sprites is less than the combined radii of their
                        # bounding circles, an overlap is present
                        
                        # Check the types of the sprites
                        if isinstance(sprite1, pellet.Pellet) and isinstance(sprite2, pacMan.PacMan):
                            # Remove the sprite's drawing and the remove the sprite from the spriteList
                            sprite1.undraw()
                            self.spriteList.remove( sprite1 )
                        elif isinstance(sprite1, pacMan.PacMan) and isinstance(sprite2, pellet.Pellet):
                            # Even after being undrawn, the pellets redraw themselves because they're still part of the 2d list in the main file. 
                            sprite2.undraw()
                            self.spriteList.remove( sprite2 )
                        else:
                            pass
                    
            