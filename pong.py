import turtle
# for graphics

window = turtle.Screen()
window.title("Ping-pong")
window.bgcolor("black")
window.setup(width=1000, height=800)
window.tracer(0)  # stops the window from updating, game is faster


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # max possible speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)  # by default 20x20
paddle_a.penup()  # do not draw a line
paddle_a.goto(-450, 0)



# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # max possible speed
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)  # by default 20x20
paddle_b.penup()  # do not draw a line
paddle_b.goto(450, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)  # max possible speed
ball.shape("circle")
ball.color("white")
ball.penup()  # do not draw a line


# main game loop
while True:
    window.update()


