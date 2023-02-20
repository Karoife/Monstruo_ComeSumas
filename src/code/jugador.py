# ----------------------------------------------
# Author:   Jose Rodolfo //  Fernando Vargas
# Date:     16/02/2023
# Version:  1.0
# ----------------------------------------------
# Clase Jugador
# Utilizada para guardar los puntajes
# ----------------------------------------------


class Jugador:

    # Funcion constructora de la clase
    def __init__(self, id, nombre):
        self.puntaje = 0
        self.id = id
        self.nombre = nombre
        self.pos = 0

    # Funcion que devuelve el nombre del jugador
    def getNombre(self):
        return self.nombre

    # Funcion que regresa el ID
    def getId(self):
        return self.id

    # Funcion que regresa el Puntaje
    def getPuntaje(self):
        return self.puntaje

    # Funcion que establece el puntaje
    def setPuntaje(self, puntajeNuevo):
        self.puntaje = puntajeNuevo

    # Funcion que establece la posicion
    def setPos(self, pos):
        self.pos = pos

    # Funcion que regresa la posicion
    def getPos(self):
        return self.pos
