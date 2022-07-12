from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)



snake=Snake()
food=Food()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
scoreboard=Scoreboard()

is_on=True

while(is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.scores()


    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        is_on=False
        scoreboard.gameover()


    for seg in snake.segment:
        if(seg==snake.head):
            pass
        elif (snake.head.distance(seg)<5):
            is_on=False
            scoreboard.gameover()

screen.exitonclick()