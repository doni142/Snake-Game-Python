import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

"""Kijelző"""
screen = Screen()
screen.setup(600, 600)  # width= , height=
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

"""Class-ok használata"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""snake moves"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""Menjen a játék"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food. Ütközés észlelése kajával!
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall. Ütközés észlelése a fallal!
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
        game_is_on = False
        scoreboard.game_over()
        #snake.reset()

    # Detect collision with tail. Ütközés kigyóval.
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        # pass
        if snake.head.distance(segment) < 10:  # if head collides with any segment in the tail:
            game_is_on = False
            scoreboard.game_over()  # trigger game_over
            #snake.reset()

"""snake_2 = Turtle("square")
snake_2.color("white")
snake_2.goto(x=-20, y=0)
snake_3 = Turtle("square")
snake_3.color("white")
snake_3.goto(x=-40, y=0)"""

screen.exitonclick()
