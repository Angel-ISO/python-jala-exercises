import time

class ReproductorDeMusica:
    def __init__(self):
        self.en_reproduccion = False
        self.tiempo_restante = 0

    def reproducir(self, cancion, duracion):
        if not self.en_reproduccion:
            self.en_reproduccion = True
            self.tiempo_restante = duracion
            print(f'Reproduciendo: {cancion}')
            self.iniciar_temporizador()

    def iniciar_temporizador(self):
        while self.en_reproduccion and self.tiempo_restante > 0:
            print(f'Tiempo restante: {self.tiempo_restante} segundos')
            time.sleep(1)
            self.tiempo_restante -= 1
        if self.en_reproduccion:
            print('Canción terminada')
            self.en_reproduccion = False

    def pausar(self):
        if self.en_reproduccion:
            self.en_reproduccion = False
            print('Pausado')

reproductor = ReproductorDeMusica()
reproductor.reproducir('Rap The F', 10)  
time.sleep(3)  
reproductor.pausar()
