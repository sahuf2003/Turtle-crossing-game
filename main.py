from turtle import Screen
from turt import User
from car import Car_manager
from scoreboard import Scoreboard
import time
import random


def ray():
    random_y = random.randint(-200, 250)
    return random_y


screen = Screen()
screen.title("Turtle crossing game")
screen.setup(600, 600)
screen.tracer(0)
scoreboard = Scoreboard()
user = User()
car_manager = Car_manager()
screen.listen()
screen.onkey(user.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # for i in range(10):
    #     cars[i].move()
    #     if cars[i].xcor() < -300:
    #         cars[i].goto(rax(),ray())
    #         cars[i].color(random.choice(color_list))
    #

    #     user.goto(0,-280)
    #     for i in range(10):
    #         cars[i].increase_speed()
    # for i in cars:
    #     if user.distance(i) < 28:
    #         game_is_on = False
    #         scoreboard.game_over()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(user) < 20:
            game_is_on = False
            scoreboard.game_over()


    if user.ycor() > 280:
        scoreboard.increase_score()
        user.goto(0, -280)
        car_manager.increase_speed()
    screen.update()

screen.exitonclick()
