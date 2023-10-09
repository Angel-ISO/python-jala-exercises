#creo mi clase o objeto implementando adstracion

class character:
    #asigno el primer metodo(el constructor en este caso) y le paso argumentos propios del objeto
    def __init__ (self, tula, nombre,fuerza, inteligencia, agilidad, defensa, vida):
        self.tula = tula
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.defensa = defensa
        self.vida = vida


    # defino un metodo para poder ingresar a  los valores
    def atributos (self): 
       print(self.nombre, ":", sep="") # el sep lo uso para establecer un separador entre las cadenas.
       print("-Fuerza:", self.fuerza)
       print("-inteligencia", self.inteligencia)
       print("-agilidad", self.agilidad)
       print("-defensa", self.defensa)
       print("-vida", self.vida)

     #creo un nuevo metodo que me permite asignarle 1 punto extra de los valores a los cuales accedo con self
    def Upgrades (self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    #aqui intento revisar que el personaje no tenga la vida mas baja del estandar permitido
    def StillAlive (self):
        if self.vida > 0:
            return True
        else:
            return False
       #finalmente aqui pregunto si continua con vida. en caso contrario puede seguir luchando 
    def isDead(self):
        self.vida = 0
        print(self.nombre, " murio")

   #ademas aqui establesco un metodo(funcion) que me sirve para poder capturar los valores
    def daño (self, enemigo):
        return self.fuerza - enemigo.defensa
    #y finalmente aqui reasigno los valores de vida para que se refresquen lo datos correctamente
    def atacar (self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print (self.nombre, " realizaste", daño, "puntos de daño a", enemigo.nombre)
        
#creo mis personajes

Personaje = character(17,"mata vacas", 10, -1, 4, 6, 100)
enemigo = character(2,"roba guarderias", 6, 1, 5, 4, 85)      

#realizo un ataque donde la fuerza del atacante se le restara a la vida del contrincante
Personaje.atacar(enemigo)  
enemigo.atributos()
f  