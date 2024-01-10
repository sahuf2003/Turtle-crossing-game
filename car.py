from turtle import Turtle
COLOR_LIST = ['blue','green','red','yellow','purple']
MOVE_DISTANCE = 5
SPEED = 10
import random

class Car_manager:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_DISTANCE

    def create_cars(self):
        ran = random.randint(1,6)
        if ran == 6:
            new_car = Turtle("square")
            random_y = random.randint(-250,250)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.goto(250,random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)
    def increase_speed(self):
        self.car_speed += SPEED
