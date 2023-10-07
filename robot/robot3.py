class Part:
    def __init__(self, name, attack_level, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        self.available = True

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.available,
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption
        }

    def is_available(self):
        return self.defense_level > 0

colors = {
    "Black": "\x1b[90m",
    "Blue": "\x1b[94m",
    "Cyan": "\x1b[96m",
    "Green": "\x1b[92m",
    "Magenta": "\x1b[95m",
    "Red": "\x1b[91m",
    "White": "\x1b[97m",
    "Yellow": "\x1b[93m"
}

class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = colors[color_code]
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=15),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=5, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15)
        ]

    def greet(self):
        print("Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, "percent energy left")

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_robot.parts[part_to_attack].defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_use].energy_consumption

    def is_on(self):
        return self.energy >= 0

    def is_there_available_parts(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def print_status(self):
        print(self.color_code)
        robot_art = "{:<12} {:<10} {:<10} {:<18}"
        headers = robot_art.format("Part Name", "Status", "Attack", "Defense")
        print(headers)
        for part in self.parts:
            status_dict = part.get_status_dict()
            print(robot_art.format(part.name, status_dict["{}_status".format(part.name.replace(" ", "_").lower())], status_dict["{}_attack".format(part.name.replace(" ", "_").lower())], status_dict["{}_defense".format(part.name.replace(" ", "_").lower())]))
        print(colors["Black"])

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

def play():
    playing = True
    print("Welcome to the game")
    robot_one = Robot("Jarvis", "Cyan")
    robot_two = Robot("Friday", "Red")
    round = 2
    
    while playing:
        if round % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        
        current_robot.print_status()
        print("What part should I use to attack?")
        part_to_use = input("Choose a part number: ")
        part_to_use = int(part_to_use)

        enemy_robot.print_status()
        print("Which part of the enemy should we attack?")
        part_to_attack = input("Choose an enemy part to attack: ")
        part_to_attack = int(part_to_attack)

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        round += 1
        
        if not enemy_robot.is_on() or not enemy_robot.is_there_available_parts():
            playing = False
            print("Congratulations, you won")
            print(current_robot.name)

play()
