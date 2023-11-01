from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 23, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.display_score()

    def display_score(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def start_timer(self):
        self.goto(0, 0)
        for i in range(3, 0, -1):
            self.clear()
            self.write(f"{i}", align=ALIGNMENT, font=("Courier", 40, "bold"))
            time.sleep(0.8)
        self.clear()
        self.display_score()



