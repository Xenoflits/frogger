COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self,level):
        super().__init__()
        self.color(COLORS[random.randint(0,len(COLORS)-1)])
        print(f'{self.color}')
        self.left(180)
        self.pu()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y = random.randint(-150,150)
        self.goto(300, self.y)
        self.level = level

    def move(self):
        self.forward(MOVE_INCREMENT*self.level+STARTING_MOVE_DISTANCE)


