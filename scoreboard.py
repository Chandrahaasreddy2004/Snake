from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = -1
        self.scores()


    def scores(self):

        self.score+=1

        self.clear()
        self.write(arg=f"score:{self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game over", align="center", font=("Arial", 20, "normal"))

