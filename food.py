from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)        # 10*10px turtle (Normally its 20*20px)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
