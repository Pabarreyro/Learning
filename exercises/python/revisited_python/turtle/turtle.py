import turtle

# Inside python standard is "turtle", inside which is the class Turtle
# def draw_square():
#     ocean = turtle.TurtleScreen()  # Create a window screen
#     ocean.bgcolor("blue")  # Make it blue
#
#     brad = turtle.Turtle()  # We're grabbing a turtle here from the __init__ funct in class
#     brad.shape = ("turtle")
#     brad.color = ("yellow")
#     brad.speed = (2)
#     brad.forward(100)  # Move it forward by 100 pixels.
#     brad.right(90)  # Turn right; four more of this
#     brad.forward(100)  # Move it forward by 100 pixels.
#     brad.right(90)  # Turn right
#     brad.forward(100)  # Move it forward by 100 pixels.
#     brad.right(90)  # Turn right
#     brad.forward(100)  # Move it forward by 100 pixels.
#     brad.right(90)  # Turn right
#
#     angie = turtle.Turtle()
#     angie.shape("arrow")
#     angie.shape("yellow")
#     angie.circle(100)
#
#     ocean.exitonclick()  # Close window whenever you want.
#
# draw_square()

# The problem is that this is very repetitive,
# and the function name does not account for drawing circle
# Below is a correction:


def square_draw(some_turtle):
    for i in range(1, 5):  # for loop applies basic moves in range (1 to n-1)
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    ocean = turtle.TurtleScreen()  # Create a window screen
    ocean.bgcolor("blue")  # Make it blue
    #  Create Brad; Brad draws squares
    brad = turtle.Turtle()  # We're grabbing a turtle here from the __init__ funct in class
    brad.shape = ("turtle")  # One of many attributes related to turtle.Turtle()
    brad.color = ("yellow")
    brad.speed = (2)
    for i in range(1, 37): # for loop creates circle of squares
        square_draw(brad)
        brad.right(10)  # turns brad right 10 degrees after each square

    #   Create Angie; Angie draws circles
    angie = turtle.Turtle()  # Another object/instance of class Turtle()
    angie.shape("arrow")  # Attribute of the same class Turtle()
    angie.shape("yellow")
    angie.circle(100)

    ocean.exitonclick()  # Close window whenever you want.

draw_art()


#  What's happening in the background...
# class Turtle():
#     def __init__(self):