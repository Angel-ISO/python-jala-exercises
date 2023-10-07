class Flower:
    def __init__(self, name, petal_color, corolla_shape, stamens, pistils, inflorescence):
        self.name = name
        self.petal_color = petal_color
        self.corolla_shape = corolla_shape
        self.stamens = stamens
        self.pistils = pistils
        self.inflorescence = inflorescence

    """polinisadores xd"""

    def attract_pollinators(self):
        return f"{self.name} attracts pollinators with {self.petal_color} petals of {self.corolla_shape} shape."

    def reproduce(self):
        if self.pistils == 1:
            return f"{self.name} reproduces with a pistil consisting of an enlarged area containing ovules and a style with a stigma at its end."
        else:
            return f"{self.name} reproduces with a pistils consisting of an enlarged area containing ovules and a style with a stigma at its end."

    def __str__(self):
        return f"{self.name} - Petal Color: {self.petal_color}, Corolla Shape: {self.corolla_shape}, Stamens: {self.stamens}, Pistils: {self.pistils}, Inflorescence: {self.inflorescence}"




