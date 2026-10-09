import turtle

#next up we will set up the game window
window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800, height=600)
window.tracer(0) #this reduces delays in the game
window.bgcolor("black")

#game items
ball = turtle.Turtle()
ball.speed(0) #fastest
ball.shape("circle")
ball.color("pink")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(x=0, y=0)
ball.penup()
ball_dx, ball_dy = 0.2, 0.2
ball_speed = 0.5

center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_wid=25, stretch_len=.1)
center_line.penup()
center_line.goto(x=0, y=0)

#player1
Player1 = turtle.Turtle()
Player1.speed(0)
Player1.shape("square")
Player1.color("#cba4eb")
Player1.shapesize(stretch_wid=6, stretch_len=0.5)
Player1.penup()
Player1.goto(x=-350, y=0)

#player2
Player2 = turtle.Turtle()
Player2.speed(0)
Player2.shape("square")
Player2.color("#bfd7db")
Player2.shapesize(stretch_wid=6, stretch_len=0.5)
Player2.penup()
Player2.goto(x=350, y=0)

#score
score = turtle.Turtle()
score.speed(0)
score.color("#fa7ad4")
score.penup()
score.goto(x=0, y=260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 12, "normal"))
score.hideturtle()
P1SCORE, P2SCORE = 0, 0

#Player Movements
PS = 20 #Player Speed

def Player1_up():
    Player1.sety(Player1.ycor() + PS)

def Player1_down():
    Player1.sety(Player1.ycor() - PS)

def Player2_up():
    Player2.sety(Player2.ycor() + PS)

def Player2_down():
    Player2.sety(Player2.ycor() - PS)

#controls (make sure keyboard is on English mode and off caps lock)
window.listen()
window.onkeypress(Player1_up, "w")
window.onkeypress(Player1_down, "s")
window.onkeypress(Player2_up, "Up")
window.onkeypress(Player2_down, "Down")

#game loop
while True:
    window.update()
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))
    if(ball.ycor() > 290):
        ball.sety(290)
        ball_dy *= -1

    if(ball.ycor() < -290):
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (Player1.ycor()-60) and ball.ycor() < (Player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (Player2.ycor()-60) and ball.ycor() < (Player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        P1SCORE += 1
        score.write(f"Player 1: {P1SCORE}  Player 2: {P2SCORE}", align="center", font=("Courier", 12, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        P2SCORE += 1
        score.write(f"Player 1: {P1SCORE}  Player 2: {P2SCORE}", align="center", font=("Courier", 12, "normal"))