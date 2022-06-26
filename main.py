from turtle import Screen
import snake
import time
from food import Food
from scoreboard import Scoreboard


# set up the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Attack")
screen.tracer(0)

snake = snake.Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.game_over()
        game_is_on = False

    # Detect collision with tail using list slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

    # if the head collides with any section of the tail, we trigger game over:
        # trigger game_over



















screen.exitonclick()
