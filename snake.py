from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add(position)


    def add(self,position):
        chandu = Turtle()
        chandu.color("white")
        chandu.shape("square")
        chandu.penup()
        chandu.goto(position)
        self.segment.append(chandu)


    def extend(self):
        self.add(self.segment[-1].position())


    def move(self):
        for seg in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(90)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(270)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(0)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(180)