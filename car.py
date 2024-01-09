from turtle import Turtle
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.goto(280,0)
    def move(self):
        self.new_x = self.xcor() - 10
        self.goto(self.new_x,self.ycor())
    def increase_speed(self):
        self.new_x *= 0.9
        self.move()