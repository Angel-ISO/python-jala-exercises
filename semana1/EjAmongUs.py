class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_impostor = False
        self.tasks = []

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def sabotage(self, sabotage_type):
        if self.is_impostor:
            pass

    def report(self, player):
        pass

    def vote(self, player):
        pass

""" generamos los jugadores """
player1 = Player("Player 1", "Red")
player2 = Player("Player 2", "Blue")
player3 = Player("Player 3", "Green")
player4 = Player("Player 4", "Yellow")

""" aqui asigno el rol impostor a 2 jugadores """

player1.is_impostor = True
player4.is_impostor = True


""" y finalmente le muestro las tareas respectivas a cada uno """

player1.tasks = ["Fix Wiring", "Download Data", "Empty Garbage"]
player2.tasks = ["Fix Wiring", "Admin Swipe Card"]
player3.tasks = ["Download Data", "Empty Garbage"]
player4.tasks = ["Sabotage Reactor", "Admin Swipe Card"]
