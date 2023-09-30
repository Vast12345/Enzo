import turtle
t = Turtle()
# Draw a line from (x1, y1) to (x2, y2)
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a string s at the specified location (x, y)
def write_texts(s, x , y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Put the pen down
    turtle.write(s)

# Draw a point at the specified location (x, y)
def draw_point(x, y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Put the pen down
    turtle.begin_fill() # Begin the fill color shape
    turtle.circle(3)
    turtle.end_fill() # Fill the shape

# Draw a circle centered at (x, y) with the specified radius
def draw_circle(x = 0, y = 0, radius = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Put the pen down
    turtle.circle(radius)

# Draw a rectangle at (x, y) with the specified width and height
def draw_rectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Put the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
linex1 = 1
liney1 = 3
linex2 = 2
liney2 = 4
line = draw_line(linex1, liney1, linex2, liney2)

    