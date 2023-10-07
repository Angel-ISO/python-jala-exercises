""" defino la clase y añado los atributos en un array """

class RockPaperScissorsGame:
    def __init__(self):
        self.RulesOfGame = ["rock", "paper", "scissors"]

    def selectRule(self, player_number):
        while True:
            choice = input(f"welcome please player {player_number}, choose rock, paper, or scissors: ").lower()
            if choice in self.RulesOfGame:
                return choice
            else:
                print("Please choose a correct option: rock, paper, or scissors.")

    def GetChampion(self, FirstP, SecondP):
        if FirstP == SecondP:
            return "WOW! we have a draw"
        elif (FirstP == "rock" and SecondP == "scissors") or \
             (FirstP == "paper" and SecondP == "rock") or \
             (FirstP == "scissors" and SecondP == "paper"):
            return "First player"
        else:
            return "Second player"

    def ResultGame(self):
        FirstPlayer = self.selectRule(1)
        SecondPlayer = self.selectRule(2)

        result = self.GetChampion(FirstPlayer, SecondPlayer)

        print(f"{result} is the winer. Congratulations!")

Result = RockPaperScissorsGame()
Result.ResultGame()


