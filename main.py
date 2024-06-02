import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move_turtle,"Up")
counter = 0
game_is_on = True


carmanager = []
while game_is_on:
    time.sleep(0.1)
    if player.ycor() > 240:
        scoreboard.level_up()
        player.goto(0,-200)
        
    interval = random.randint(1,3)
    counter += interval
    if counter % 10 == 0:
        car = CarManager(scoreboard.level)
        carmanager.append(car)
    for carman in carmanager:
        if(carman.distance(player) < 20):
            scoreboard.write_game_over()
            game_is_on = False
        carman.move()            
        
    screen.update()

screen.exitonclick()