from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #it turns the turtle graphics animation on or off

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True #For game to start and to end
while game_is_on:
    screen.update() #used to refresh the scrreen after every change
    time.sleep(0.1) #It delays the execution for the given number of seconds, i.e to reduce the speed of snake
    snake.move()


    # Detect collision with food
    if snake.head.distance(food) < 15: # distance between turtle and food
        food.refresh()
        snake.extend()
        score.clear()
        score.increase_score()

    # Detect collision
    if snake.head.xcor() <-295 or snake.head.xcor() > 295 or snake.head.ycor() <- 295 or snake.head.ycor() > 295:
        score.reset()
        snake.reset()


    # Detect collision with tail
    for segments in snake.segment[1:]:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

    # If head collides with any segment in the tail then it is game over


































screen.exitonclick()