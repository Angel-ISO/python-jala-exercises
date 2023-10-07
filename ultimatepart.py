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


class PartPiece:
    def __init__(self, name, effect, attack_level=0, defense=0):
        self.name = name
        self.effect = effect
        self.attack_level = attack_level
        self.defense = defense


    def is_available(self):
        return self.defense <= 0
    

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}
"""



class Robot:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
        ]
        self.inventory = {}

    def greet(self):
        print("Hello, my name is", self.name)

    def print_energy(self):
        print("We have", self.energy, "percent energy left")

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        enemy_part = enemy_robot.parts[part_to_attack]
        enemy_part.defense_level -= self.parts[part_to_use].attack_level
        self.energy -= self.parts[part_to_use].energy_consumption

        if enemy_part.defense_level <= 0:
            self.inventory.append(PartPiece(enemy_part.name, enemy_part.attack_level, enemy_part.defense))

    def is_on(self):
        return self.energy >= 0

    def is_there_available_parts(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def print_status(self):
        part = self.parts[0]
        print(robot_art.format(
            head_name=part.name,
            head_status=part.available,
            head_attack=part.attack_level,
            head_defense=part.defense_level,
            head_energy_consump=part.energy_consumption
        ))

def play():
    playing = True
    print("Welcome to the game")
    robot_one = Robot("Jarvis")
    robot_two = Robot("Frida")
    round = 1

    while playing:
        if round % 2 == 1:
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

        if 0 <= part_to_use < len(current_robot.parts) and 0 <= part_to_attack < len(enemy_robot.parts):
            current_robot.attack(enemy_robot, part_to_use, part_to_attack)

            if not enemy_robot.is_on() or not enemy_robot.is_there_available_parts():
                playing = False
                print("Congratulations, you won")
                print(current_robot.name)
            elif not current_robot.is_on() or not current_robot.is_there_available_parts():
                playing = False
                print("Game over! The enemy won.")
        else:
            print("Invalid part number. Please choose a valid part.")

        round += 1


play()
