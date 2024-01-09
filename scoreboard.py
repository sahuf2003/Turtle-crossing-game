from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 0
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write(f"Level:{self.level}",False,"left",("Cambria",24,"normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}",False,"left",("Cambria",24,"normal"))
    def increase_score(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER",False,"center",("Arial",32,"normal"))

