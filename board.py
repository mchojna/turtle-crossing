import turtle


class Board:

    def __init__(self, level_num, lives_num):
        self.level_num = level_num
        self.lives_num = lives_num
        self.text = turtle.Turtle()

    def create(self):
        self.text.clear()
        self.text.penup()
        self.text.hideturtle()

        self.text.setposition(-338, 264)
        self.text.color("white")
        self.text.write(arg=f"Level: {self.level_num}", move=False, align="center", font=("Super Effective", 30, "normal"))

        self.text.setposition(-340, 229)
        self.text.color("white")
        self.text.write(arg=f"Lives: {self.lives_num}", move=False, align="center", font=("Super Effective", 30, "normal"))

        self.text.setposition(329, -267)
        self.text.color("white")
        self.text.write(arg=f"START", move=False, align="center", font=("Super Effective", 25, "normal"))

        self.text.setposition(330, 249)
        self.text.color("white")
        self.text.write(arg=f"FINISH", move=False, align="center", font=("Super Effective", 25, "normal"))

    def next(self):
        self.text.clear()
        self.text.penup()
        self.text.hideturtle()

        self.text.setposition(0, -35)
        self.text.color("white")
        self.text.write(arg=f"NEXT LEVEL!", move=False, align="center", font=("Super Effective", 80, "normal"))

    def over(self):
        self.text.clear()
        self.text.penup()
        self.text.hideturtle()

        self.text.setposition(0, -35)
        self.text.color("white")
        self.text.write(arg=f"GAME OVER!", move=False, align="center", font=("Super Effective", 80, "normal"))

    def end(self):
        self.text.clear()
        self.text.penup()
        self.text.hideturtle()

        self.text.setposition(0, -35)
        self.text.color("white")
        self.text.write(arg=f"THE END!", move=False, align="center", font=("Super Effective", 80, "normal"))
