import random

class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = int(input("Ingrese el nivel de habilidad del jugador {}: ".format(self.nombre)))

    def golpear(self, pelota):
        fuerza = random.randint(1, 10)
        direccion = random.choice(["derecha", "izquierda"])
        return fuerza, direccion

class Pelota:

    def __init__(self, posicion, velocidad):
        self.posicion = posicion
        self.velocidad = velocidad

    def mover(self):
        self.posicion = (self.posicion[0] + self.velocidad[0], self.posicion[1] + self.velocidad[1])

class JuegoTenis:

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.pelota = Pelota((0, 0), (0, 0))
        self.puntos_para_ganar = 4

    def jugar(self):
        while True:
            fuerza_jugador1, direccion_jugador1 = self.jugador1.golpear(self.pelota)
            fuerza_jugador2, direccion_jugador2 = self.jugador2.golpear(self.pelota)

            self.pelota.mover()

            if self.pelota.posicion[0] < 0 or self.pelota.posicion[0] > 10 or self.pelota.posicion[1] < 0 or self.pelota.posicion[1] > 10:
                if direccion_jugador1 == direccion_jugador2:
                    return "Empate"
                else:
                    if direccion_jugador1 == "derecha":
                        return "Jugador 1"
                    else:
                        return "Jugador 2"

            if self.pelota.posicion[0] > 5 and self.pelota.posicion[0] < 7 and self.pelota.posicion[1] > 2 and self.pelota.posicion[1] < 8:
                if direccion_jugador1 == "izquierda":
                    return "Jugador 2"
                else:
                    return "Jugador 1"


if __name__ == "__main__":
    jugador1 = Jugador("Juan")
    jugador2 = Jugador("Pedro")
    juego = JuegoTenis(jugador1, jugador2)
    resultado = juego.jugar()
    print(resultado)
