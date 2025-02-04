STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.goto(STARTING_POSITION)
        self.left(90)
    
    def move_turtle(self):
        print(self.xcor())
        self.forward(10)