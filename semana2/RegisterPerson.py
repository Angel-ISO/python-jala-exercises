import json

class Segip:
    def __init__(self):
        self.registry = {}
        self.json_file = "data.json"

        try:
            with open(self.json_file, "r") as file:
                self.registry = json.load(file)
        except FileNotFoundError:
            pass

    def add_person(self):
        name = input("Enter the person's name: ")
        id_card = input("Enter the ID card number (must have 8 digits): ")

        if not id_card.isdigit() or len(id_card) != 8:
            print("Invalid ID card, it must have 8 digits.")
        elif id_card in self.registry.values():
            print("Duplicate ID card.")
        else:
            self.registry[name] = id_card
            print(f"{name} has been registered with ID card {id_card}.")

            with open(self.json_file, "w") as file:
                json.dump(self.registry, file)

    def check_person(self, name):
        if name in self.registry:
            print(f"{name}'s ID card is {self.registry[name]}.")
        else:
            print(f"{name} is not registered in SEGIP.")

segip = Segip()
segip.add_person()
name_to_check = input("Enter the name to check the ID card: ")
segip.check_person(name_to_check)
