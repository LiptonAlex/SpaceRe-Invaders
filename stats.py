class Stats (): #Statistics class
    def __init__(self):
        "Initiation of Stats"
        self.reset_stats()
        self.run_game = True
        with open('HighScore.txt', 'r') as high:
            self.high_score = int(high.readline())

    def reset_stats(self): #dynamic stats of gun
        self.guns_left = 2
        self.score = 0