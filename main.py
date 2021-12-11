from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

TIME = 0.1

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game logic
game_on = True

while game_on:
    screen.update()
    time.sleep(TIME)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        # game_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Left", fun=snake.left)

screen.exitonclick()
