from screen import Screen, Line
from player import Player
from board import Board
from enemy import Enemy

screen = Screen()
screen.create()
screen.listen()

line = Line()
line.create()

board = Board(level_num=1, lives_num=3)
board.create()

enemy = Enemy()

game = True
end = False
level_1 = True

player = Player()
player.create()
screen.move(key="space", fun=player.move)
screen.move(key="w", fun=player.up)
screen.move(key="a", fun=player.left)
screen.move(key="d", fun=player.right)


def next_level():
    board.level_num += 1
    enemy.clean()
    player.create()
    board.create()


def level(speed):
    global level_1
    global level_2
    global level_3
    global game

    enemy.create()
    enemy.move(speed)

    for element in enemy.enemies:
        if player.player.distance(element) < 30:
            board.lives_num -= 1
            if board.lives_num > 0:
                enemy.clean()
                player.create()
                board.create()
            else:
                board.over()
                level_1 = False
                level_2 = False
                level_3 = False
                game = False
                break


while game:

    while level_1:
        level(60)

        if player.player.ycor() >= 220:
            level_1 = False
            level_2 = True
            board.next()
            break

    if level_2:
        next_level()

    while level_2:
        level(80)

        if player.player.ycor() >= 220:
            level_2 = False
            level_3 = True
            board.next()
            break

    if level_3:
        next_level()

    while level_3:
        level(120)

        if player.player.ycor() >= 220:
            level_3 = False
            game = True
            board.end()
            break

screen.exit()
