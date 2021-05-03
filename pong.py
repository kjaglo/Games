import turtle
# for graphics
import winsound
# for interacting with the operating system

# Parameters

speed_x = 1/4
speed_y = 1/4


# Dimension
width = 1000
height = 800

# Score
score_a = 0
score_b = 0

window = turtle.Screen()
window.title("Ping-pong")
window.bgcolor("black")
window.setup(width=width, height=height)
window.tracer(0)  # stops the window from updating, game is faster

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # max possible speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)  # by default 20x20
paddle_a.penup()  # do not draw a line
paddle_a.goto(-width / 2 + 50, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # max possible speed
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)  # by default 20x20
paddle_b.penup()  # do not draw a line
paddle_b.goto(width / 2 - 50, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)  # max possible speed
ball.shape("circle")
ball.color("white")
ball.penup()  # do not draw a line
ball.dx = speed_x
ball.dy = speed_y

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)

# functions


def paddle_a_up():
    y = paddle_a.ycor()  # returns y coordinate
    if y < height / 2 - 7 * 10:
        y += 10
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # returns y coordinate
    if y > -height / 2 + 8 * 10:
        y -= 10
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # returns y coordinate
    if y < height / 2 - 7 * 10:
        y += 10
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # returns y coordinate
    if y > -height / 2 + 8 * 10:
        y -= 10
        paddle_b.sety(y)


def pen_update():
    pen.clear()
    pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Keyboard binding

window.listen()  # listen for a keyboard input
window.onkeypress(paddle_a_up, 'w')  # when a user presses 'w' call function up
window.onkeypress(paddle_a_down, 's')  # when a user presses 'w' call function up
window.onkeypress(paddle_b_up, 'Up')  # when a user presses 'w' call function up
window.onkeypress(paddle_b_down, 'Down')  # when a user presses 'w' call function up

# print(help(paddle_a.ycor))

pen_update()

# main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # game over and play again
    if ball.xcor() > width / 2 - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 10
        pen_update()

    if ball.xcor() < -width / 2 + 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 10
        pen_update()

    # border checking
    if ball.ycor() > height / 2 - 10:
        ball.sety(height / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -height / 2 + 20:
        ball.sety(-height / 2 + 20)
        ball.dy *= -1

    # paddle - ball collisions
    if (ball.xcor() > 440 and ball.xcor() < 450) and (
            ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(440)
        ball.dx *= -1
        score_b += 1
        pen_update()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -440 and ball.xcor() > -450) and (
            ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-440)
        ball.dx *= -1
        score_a += 1
        pen_update()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # print("BALL x:", ball.xcor(), "y:", ball.ycor())
    # print("PADDLE B x:", paddle_b.xcor(), "y:", paddle_b.ycor())
    # print("-" * 30)

# paddle_b 330 up to -320
