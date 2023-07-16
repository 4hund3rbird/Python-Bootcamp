from turtle import Turtle



class Scorecard(Turtle):

    def __init__(self,score,highscr) -> None:
        super().__init__()
        self.score=score
        self.highscore=highscr
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.color("white")
        style=('Arial', 20, 'bold')
        self.write(f"Score : {score}  Highscore :{self.highscore}",font=style,align="center")

    def high_score(self):
        if self.score>=self.high_score:
            self.high_score=self.score

    def game_over(self):
        self.pu()
        self.goto(0,0)
        self.color("white")
        style=('Arial', 30, 'bold')
        self.write(f"GAME OVER!! :(\nYour final score is {self.score}.\n ",font=style,align="center")

        