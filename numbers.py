"""A list of methods to make keeping score easier"""

def draw1(turt):
    # Assume the turtle is facing north for all of these functions
    turt.forward(.2)

def draw2(turt):
    distance = .1
    print("1)")
    turt.penup()
    turt.forward(.2)
    turt.pendown()
    print("2)")
    turt.right(90)
    turt.forward(distance)
    turt.right(90)
    turt.forward(distance)
    turt.right(90)
    turt.forward(distance)
    turt.left(90)
    turt.forward(distance)
    turt.left(90)
    turt.forward(distance)

def draw3():
    pass

def draw4():
    pass

def draw5():
    pass