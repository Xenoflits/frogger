FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(0,250)
        self.write_level()


    def level_up(self):
        self.level += 1
        
        self.write_level()
    def write_level(self):
        self.clear()
        
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def write_game_over(self):
        self.clear()
        self.write(f"GAME OVER", font=FONT, align='center')