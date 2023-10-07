class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 102
        print("Hello world")


def greet(self):
    print("Hello, my name is", self.name)


def print_energy(self):
    print("We have", self.energy, "percent energy left")



def is_on(self):
    if self.energy > 0:
        return True
    else:
        return False



friday = Robot("Friday")
friday.greet()

on = friday.is_on()
print(on)
