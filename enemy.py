import turtle
import random


class Enemy:

    def __init__(self):
        self.enemies = []

    def create(self):
        x_cor = 400
        y_prev = 0

        while True:
            y_cor = random.choice([-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200])
            if y_cor != y_prev:
                y_prev = y_cor
                break

        enemy = turtle.Turtle()
        enemy.hideturtle()
        enemy.penup()

        turtle.colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        enemy.color((r, g, b))

        enemy.shape("square")
        enemy.speed(0)
        enemy.shapesize(1, 2)
        enemy.setposition(x_cor, y_cor)
        enemy.setheading(180)
        enemy.showturtle()
        self.enemies.append(enemy)

    def move(self, distance):
        for num in range(len(self.enemies) - 1):
            if self.enemies[num].xcor() > -420:
                self.enemies[num].forward(distance)

    def clean(self):
        for element in self.enemies[:-1]:
            element.hideturtle()
            self.enemies.remove(element)
