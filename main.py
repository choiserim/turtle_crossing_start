import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()

level_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            level_board.game_over()
            game_is_on = False

    # detect successful crossing
    if player.is_at_finish_line():
        level_board.increase_level()
        player.go_to_start_line()
        car_manager.speed_up()

screen.exitonclick()


