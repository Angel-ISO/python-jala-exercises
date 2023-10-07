class GameSecondVersion:
    def __init__(self):
        self.rules = {
            "rock": {"scissors", "Sword"},
            "paper": {"rock", "Spock"},
            "scissors": {"paper", "Sword"},
            "Sword": {"Spock", "paper"},
            "Spock": {"scissors", "rock"},
        }

    def select_rule(self, player_number):
        while True:
            choice = input(f"Welcome, Player {player_number}, choose rock, paper, scissors, Sword, or Spock: ").lower()
            if choice in self.rules:
                return choice
            else:
                print("Please choose a valid option: rock, paper, scissors, Sword, or Spock.")

    def determine_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return "It's a draw!"
        elif player2_choice in self.rules[player1_choice]:
            return "Player 1"
        else:
            return "Player 2"

    def DefineTurns(self):
        player1_choice = self.select_rule(1)
        player2_choice = self.select_rule(2)

        winner = self.determine_winner(player1_choice, player2_choice)

        print(f"{winner} wins. Congratulations!")

if __name__ == "__main__":
    result = GameSecondVersion()
    result.DefineTurns()
