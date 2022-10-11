import turtle
import random


class Screen:

    def __init__(self):
        self.screen = turtle.Screen()

    def create(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")

    def listen(self):
        self.screen.listen()

    def update(self):
        self.screen.update()

    def move(self, key, fun):
        self.screen.onkey(key=key, fun=fun)

    def exit(self):
        self.screen.exitonclick()


class Line:

    def __init__(self):
        self.line = turtle.Turtle()

    def create(self):
        self.line.hideturtle()
        self.line.penup()
        self.line.pencolor("white")
        self.line.speed(0)
        self.line.setheading(180)

        y_cor = -220
        lines = 12

        for num in range(lines):

            if num % 2 == 0:
                self.line.pensize(2)
            else:
                self.line.pensize(1)

            x_cor = random.randint(375, 395)
            self.line.setposition(x_cor, y_cor)
            for _ in range(21):
                self.line.pendown()
                self.line.forward(20)
                self.line.penup()
                self.line.forward(20)
            self.line.penup()
            y_cor += 40
