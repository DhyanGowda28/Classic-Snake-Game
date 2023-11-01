from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)    # To not show animation

snake = Snake()
food = Food()
score = Scoreboard()

# screen.textinput(title="Do you want to play the Snake Game", prompt="Press any key to start")
score.start_timer()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_game_on = True


while is_game_on:
    screen.update()         # To update the screen
    time.sleep(0.1)
    snake.move()
    snake.head.color("blue")

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.extend()


    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        print("Out of screen")

    # Detect collision with tail
    for segs in snake.segments[2:]:

        if snake.head.distance(segs) < 5:
            score.reset()
            snake.reset()
            print("Collision")


screen.exitonclick()


