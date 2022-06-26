from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.goto(0, 260)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()