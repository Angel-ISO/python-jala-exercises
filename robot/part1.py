class Part:
    def __init__(self, name, attack_level, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption
        self.available = True

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        print("{} name: {}".format(formatted_name, self.name.upper()))
        print("{} status: {}".format(formatted_name, self.available))
        print("{} attack: {}".format(formatted_name, self.attack_level))
        print("{} defense: {}".format(formatted_name, self.defense_level))
        print("{} energy consumption: {}".format(formatted_name, self.energy_consumption))



head = Part("Head", attack_level=5, defense_level=10, energy_consumption=5)
head.get_status_dict()

weapon = Part("Weapon", attack_level=15, defense_level=8, energy_consumption=2)
weapon.get_status_dict()

left_arm = Part("Left Arm", defense_level=20, energy_consumption=0)
left_arm.get_status_dict()


left_leg = Part("Left Leg", attack_level=0, defense_level=20, energy_consumption=15)
left_leg.get_status_dict()

right_leg = Part("Right Leg", attack_level=0, defense_level=28, energy_consumption=15)
right_leg.get_status_dict()
