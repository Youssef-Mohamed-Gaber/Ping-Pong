import turtle

# Building game screen
wind = turtle.Screen()  # initializes screen
wind.title("Ping Pong By M074MED")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # stops the window from updating automatically

# Game objects
# paddle1
paddle1 = turtle.Turtle()  # initializes turtle object
paddle1.speed(0)  # set the speed of the animation
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(5, 1)  # or paddle1.shapesize(stretch_wid=5, stretch_len=1)  # stretches the shape to meet the size
paddle1.penup()  # stops the object from drawing lines
paddle1.goto(-380, 0)  # set the position of the object
# paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(5, 1)
paddle2.penup()
paddle2.goto(370, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# ball speed
ball.dx = 0.5
ball.dy = 0.5
# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0   ||   Player 2: 0", align="center", font=("Courier", 24, "normal"))
# screen border
screen_border1 = turtle.Turtle()
screen_border1.shape("square")
screen_border1.color("white")
screen_border1.shapesize(0.1, 40)
screen_border1.penup()
screen_border1.goto(0, 300)

screen_border2 = turtle.Turtle()
screen_border2.shape("square")
screen_border2.color("white")
screen_border2.shapesize(0.1, 40)
screen_border2.penup()
screen_border2.goto(0, -300)


# Paddles movement
# functions


def paddle1_up():
    y = paddle1.ycor()  # get the y coordinate of the paddle1
    y += 20  # set the y to increase be 20
    paddle1.sety(y)  # set the y of the paddle1 to the new y coordinate
    # or paddle1.sety(paddle1.ycor() + 20)
    if paddle1.ycor() > 250:
        paddle1.sety(250)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20  # set the y to decrease be 20
    paddle1.sety(y)
    # or paddle1.sety(paddle1.ycor() - 20)
    if paddle1.ycor() < -250:
        paddle1.sety(-250)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)
    if paddle2.ycor() > 250:
        paddle2.sety(250)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)
    if paddle2.ycor() < -250:
        paddle2.sety(-250)


# keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(paddle1_up, "w")  # when pressing w the function paddle1_up is invoked
wind.onkeypress(paddle1_down, "s")
wind.onkeypress(paddle2_up, "Up")
wind.onkeypress(paddle2_down, "Down")


# Main game loop
def game_loop(score1=0, score2=0):
    while True:
        wind.update()  # update the screen everytime the loop run

        # move the ball
        ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and everytime loops run--->+1 y axis
        ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 and everytime loops run--->+1 x axis

        # border check , top border +300px, bottom border -300, right border +400px, left border -400px, ball is 20px
        if ball.ycor() > 290:  # if ball hit top border
            ball.sety(290)  # set y coordinate +290
            ball.dy *= -1  # reverse the y direction

        if ball.ycor() < -290:  # if ball hit bottom border
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:  # if ball hit right border
            ball.goto(0, 0)  # return ball to center
            ball.dx *= -1  # reverse the x direction
            ball.dy *= -1  # reverse the y direction
            score1 += 1
            score.clear()
            score.write("Player 1: {}   ||   Player 2: {}".format(score1, score2), align="center",
                        font=("Courier", 24, "normal"))

        if ball.xcor() < -390:  # if ball hit left border
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write("Player 1: {}   ||   Player 2: {}".format(score1, score2), align="center",
                        font=("Courier", 24, "normal"))

        # ball collision with paddles
        if (ball.xcor() > 360) and (ball.xcor() < 370) \
                and (ball.ycor() < paddle2.ycor() + 50) and (ball.ycor() > paddle2.ycor() - 50):
            ball.setx(360)
            ball.dx *= -1

        if (ball.xcor() < -370) and (ball.xcor() > -380) \
                and (ball.ycor() < paddle1.ycor() + 50) and (ball.ycor() > paddle1.ycor() - 50):
            ball.setx(-370)
            ball.dx *= -1


wind.onkeypress(game_loop, " ")
while True:
    wind.update()  # update the screen everytime the loop run
