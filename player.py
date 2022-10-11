import turtle


class Player:

    def __init__(self):
        self.player = turtle.Turtle()

    def create(self):
        self.player.hideturtle()
        self.player.penup()
        self.player.setposition(x=0, y=-245)
        self.player.setheading(90)
        self.player.shape("turtle")
        self.player.color("white")
        self.player.showturtle()

    def move(self):
        if not (self.player.xcor() >= 350 or self.player.xcor() <= -350 or self.player.ycor() >= 220):
            self.player.forward(40)

    def up(self):
        self.player.setheading(90)

    def left(self):
        self.player.setheading(180)

    def right(self):
        self.player.setheading(0)
