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
        self.llenarPrintTerm()

    def getResultados(self):
        return self.resultados

    def gerPrinTerm(self):
        return self.printTerm

    def llenarResultados(self):
        # se crea resultados para las
        # 43 casillas del tablero
        for i in range(43):
            if i == 0:
                self.resultados.append("Inicio")
            elif i == 42:
                self.resultados.append("Fin")
            elif i % 5 == 0:  # cada cinco espacios se coloca un monstruo
                self.resultados.append("Monstruo")
            else:
                self.resultados.append(random.randint(2, 1500))
                # se genera 40 numeros aleatoreos
                # para las casillas que no tienen monstruo

    def llenarPrintTerm(self):
        for i in range(43):
            if i == 0:
                self.printTerm.append("Inicio")
            elif i == 42:
                self.printTerm.append("Fin")
            elif i % 5 == 0 and i != 0:
                self.printTerm.append("Monstruo")
            else:
                self.printTerm.append(random.randint(1, self.resultados[i]))
