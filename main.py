from turtle import Screen
from padle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Tanvir's pong game")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with padle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect R paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    #Detect L paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()








screen.exitonclick()