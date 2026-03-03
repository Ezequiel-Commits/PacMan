"""A class that encapsulates the pellets that the PacMan will eat to gain points"""
import turtle
import sprite

class Pellet(sprite.Sprite):
    # Use the sprite constructor

    def updateSelf(self):
        self.x, self.y = turtle.position()
        self.draw(self.x, self.y)
    

    