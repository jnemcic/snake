from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scoreboard.txt") as scoreboard_file:
            self.highest_score = scoreboard_file.read()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if int(self.highest_score) < self.score:
            with open("scoreboard.txt", mode="w") as scoreboard_file:
                self.highest_score = str(self.score)
                scoreboard_file.write(self.highest_score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
