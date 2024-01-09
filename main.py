from turtle import Screen
from turt import User
from car import Car
from scoreboard import Scoreboard
import time
import random
color_list = ["blue","green","red","cyan","magenta","yellow","purple"]
def rax():
    random_x = random.randint(250, 300)
    return random_x
def ray():
    random_y = random.randint(-200, 250)
    return random_y
screen = Screen()
screen.title("Turtle crossing game")
screen.setup(600,600)
screen.tracer(0)
scoreboard = Scoreboard()
user = User()
cars=[]
for i in range(10):
    car = Car()
    car.color(random.choice(color_list))
    car.goto(rax(), ray())
    cars.append(car)
screen.listen()
screen.onkey(user.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.3)
    for i in range(10):
        cars[i].move()
        if cars[i].xcor() < -300:
            cars[i].goto(rax(),ray())
            cars[i].color(random.choice(color_list))

    if user.ycor() > 280:
        scoreboard.increase_score()
        user.goto(0,-280)
        for i in range(10):
            cars[i].increase_speed()
    for i in cars:
        if user.distance(i) < 30:
            game_is_on = False
            scoreboard.game_over()
    screen.update()


screen.exitonclick()