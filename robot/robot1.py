class Robot:
    def __init__(self, name, color_code ):
        self.name = "Friday"
        self.color_code = "25"
        self.energy = 162
        self.on = True
        print("Hello, world!")

    def greet(self):
        print("My name is:", self.name)
        print("My color code is:", self.color_code)
        print("My energy is:", self.energy)
        print("My status is", self.on)



friday = Robot("Friday", "25")
friday.greet()

jarvis = Robot("Jarvis", "65")
jarvis.greet()
