import random

class Car:
    def __init__(self, color, model, number):
        self.color = color
        self.model = model
        self.registration_number = number

class CarFactory:
    def __init__(self):
        self.colors = ["red", "yellow", "white"]
        self.models = ["Corolla", "Swift", "T-cross"]


    def create_random_car(self):
            color = random.choice(self.colors)
            model = random.choice(self.models)
            number = "ABC123"
            car = Car(color, model, number)
            return car
    

class CloneFinder:
    def simulate_finder(self):
        car_list = self.generate_cars()
        color = self.get_color_to_compare()
        self.find_clones_in_list(car_list, color)


