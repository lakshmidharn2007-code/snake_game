from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            contents = int(file.read())
        self.highscore = contents
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.highscore}", align="center", font=("Algerian", 14, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as files:
                files.write(str(self.highscore))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

