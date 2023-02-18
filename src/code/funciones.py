# ----------------------------------------------
# Author:   Jose Rodolfo //  Fernando Vargas
# Date:     16/02/2023
# Version:  1.0
# ----------------------------------------------
# Clase Jugador 
# Utilizada para guardar los puntajes
# ----------------------------------------------frames = []
def generarFrames():
    frames = []
    for i in range(49):
        frames[i] = "Frame" + str(i+1)
    return frames