# ----------------------------------------------
# Author:   Jose Rodolfo //  Fernando Vargas
# Date:     16/02/2023
# Version:  1.0
# ----------------------------------------------
# Clase Jugador 
# Utilizada para guardar los puntajes
# ----------------------------------------------

class Jugador:

    def __init__(self, id, nombre):
        self.puntaje = 0
        self.id = id
        self.nombre = nombre
        self.pos = 0
    
    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.id

    def getPuntaje(self):
        return self.puntaje

    def setPuntaje(self, puntajeNuevo):
        self.puntaje = puntajeNuevo
    
    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos
