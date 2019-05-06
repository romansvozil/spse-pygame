import pgzrun
from math import sin, cos

WIDTH = 800
HEIGHT = 600


paddle_image = "paddle_blu"
ball_image = "ball_blu"

keys = []


class Paddle(Actor):
    def __init__(self, image):
        super(Paddle, self).__init__(image)
        self.speed = 5
        self.x = WIDTH // 2
        self.y = HEIGHT - 20

    def update(self):
        if self.left < 0:
            self.left = 0
        if self.right > WIDTH:
            self.right = WIDTH


class Ball(Actor):
    def __init__(self, image):
        super(Ball, self).__init__(image)
        self.speed = 20
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.direction = 0

    def update(self):
        pass
        # self.x = cos(self.direction) * self.speed
        # self.y = sin(self.direction) * self.speed


paddle = Paddle(paddle_image)
ball = Ball(ball_image)


def update():
    paddle.update()
    ball.update()


def draw():
    screen.fill((255, 255, 255))
    paddle.draw()
    ball.draw()


"""
def on_key_down(key):
    global keys
    keys.append(key)

def on_key_up(key):
    global keys
    keys.remove(key)
"""


pgzrun.go()
