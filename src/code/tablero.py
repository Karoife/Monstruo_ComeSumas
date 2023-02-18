# ----------------------------------------------
# Author:   Jose Rodolfo //  Fernando Vargas
# Date:     16/02/2023
# Version:  1.0
# ----------------------------------------------
# Clase Jugador 
# Utilizada para guardar los puntajes
# ----------------------------------------------
from __future__ import annotations
import random
class Tablero:
    def __init__(self):
        self.printTerm = list()
        self.resultados = list()
        self.llenarResultados()
    def getResultados(self):
        return self.resultados
    def gerPrinTerm(self):
        return self.printTerm
    def llenarResultados(self):
        for i in range(49): # se crea resultados para las 49 casillas del tablero
            if i % 5 == 0 and i != 0: # cada cinco espacios se coloca un monstruo
                self.resultados[i] = "m"
            else:
                self.resultados[i] = random.randint(2,1500) # se genera 40 numeros aleatoreos para las casillas que no tienen monstruo
    def llenarPrintTerm(self):
        for i in range(49): 
            if i % 5 == 0 and i != 0:
                self.resultados[i] = "m"
            else:
                self.printTerm[i] = random.randint(1,self.resultados[i])