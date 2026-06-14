"""A list of methods to make keeping score easier"""

def draw1(turt):
    # Assume the turtle is facing north for all of these functions
    turt.forward(.2)

def draw2(turt):
    distance = .1
    for movement in range(3):
        turt.right(90)
        turt.forward(distance)
    turt.left(90)
    turt.forward(distance)
    turt.left(90)
    turt.forward(distance)

def draw3(turt):
    distance = .1
    for movement in range(3):
        turt.right(90)
        turt.forward(distance)
    turt.left(180)
    turt.forward(distance)
    turt.right(90)
    turt.forward(distance)
    turt.right(90)
    turt.forward(distance)

def draw4(turt):
    distance = .1
    for momvent in range(2):
        turt.forward(-distance)
        turt.left(90)
    turt.forward(-distance)
    turt.forward(distance * 2)

def draw5(turt):
    distance = .1
    turt.right(90)
    turt.forward(distance)
    turt.forward(-distance)
    turt.left(90)
    turt.forward(-distance )
    turt.penup()
    turt.forward(-distance * 2)
    turt.pendown()
    turt.right(90)
    turt.circle(distance,180)