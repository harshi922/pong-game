from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


def pong():
    # Set up screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")

    # Turn off animation
    screen.tracer(0)

    # Divider for screen
    _y = 280
    for i in range(int(600 / 40)):
        divider_turtle = Turtle("square")
        divider_turtle.penup()
        divider_turtle.color("white")
        divider_turtle.goto(0, _y)
        _y -= 40

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = ScoreBoard()
    screen.listen()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    # Game on
    is_game_on = True
    while is_game_on:
        time.sleep(ball.ball_speed)  # Increases speed of animation
        screen.update()  # Manual screen refresh updates
        ball.move_ball()

        # Wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_up_down()

        # Paddle collisions
        if ball.xcor() > 380:
            ball.reset_pos()
            scoreboard.l_point()
        if ball.xcor() < -380:
            ball.reset_pos()
            scoreboard.r_point()

        # Keep paddles inside screen
        if r_paddle.ycor() > 260:
            r_paddle.goto(r_paddle.xcor(), 260)
        if l_paddle.ycor() > 260:
            l_paddle.goto(l_paddle.xcor(), 260)
        if r_paddle.ycor() < -260:
            r_paddle.goto(r_paddle.xcor(), -260)
        if l_paddle.ycor() < -260:
            l_paddle.goto(l_paddle.xcor(), -260)

        if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
            ball.bounce_left_right()

        # Indicate win/lose
        if scoreboard.l_score > scoreboard.r_score and (scoreboard.l_score - scoreboard.r_score) >= 10:
            is_game_on = False
            scoreboard.game_over("left")
        elif scoreboard.l_score < scoreboard.r_score and (scoreboard.r_score - scoreboard.l_score) >= 10:
            is_game_on = False
            scoreboard.game_over("right")

        #  Play again
        if not is_game_on:
            user_choice = screen.textinput("Play Again ?", "Press y to play again and click on screen to exit:")
            if str(user_choice) == "y":
                screen.clear()
                pong()
            else:
                exit()
    screen.exitonclick()


pong()
