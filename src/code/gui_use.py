#!/usr/bin/python3
# ----------------------------------------------
# Author:   Jose Rodolfo //  Fernando Vargas
# Date:     16/02/2023
# Version:  1.0
# ----------------------------------------------
# Clase Jugador 
# Utilizada para guardar los puntajes
# ----------------------------------------------

import gi
import tablero
import sys
import random
import jugador

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

def main():
    #-----------------------------------------
    # Variables de la GUI
    # ----------------------------------------
    global builder
    global tableroJugar
    global frames
    global labels
    global popUp
    global labelsJugar
    global prinDatos
    global popUpCancel
    global botDado
    global labelDado
    global dado
    global ImagenesOne
    global ImagenesTwo
    global jugador1
    global jugador2
    global turno
    global entradaID
    global respuesta
    global respuestaC
    global mensaje
    global mssAceptar
    global mssAceptar2
    global flag1, flag2
    # -----------------------------------------
    # jugador1 = jugador.Jugador("4545", "Neymar")
    # jugador2 = jugador.Jugador("5656", "Juan")
    # -----------------------------------------
    builder = Gtk.Builder()
    builder.add_from_file("./src/code/GUI.glade")

    # -----------------------------------------------------
    win = builder.get_object("Ventana")
    popUp = builder.get_object("Popup")
    popUpCancel = builder.get_object("Cancelar")
    popUpUpResponder = builder.get_object("Responder")
    respuesta = builder.get_object("Respuesta")
    botDado = builder.get_object("Dado")
    labelDado = builder.get_object("DadoLabel")
    botAgregar = builder.get_object("Agregar")
    mensaje = builder.get_object("Message")
    mssAceptar = builder.get_object("MssAceptar")
    mssAceptar2 = builder.get_object("MssAceptar2")
    entradaID = builder.get_object("Entrada_ID")
    # ------------------------------------------------------
    popUpCancel.connect("clicked", cerrarPop)
    botDado.connect("clicked", lanzarDado)
    botAgregar.connect("clicked", agregarJugar)
    popUpUpResponder.connect("clicked", responderPreg)
    mssAceptar.connect("clicked", aceptarMensaje)
    mssAceptar2.connect("clicked", aceptarMensaje)

    # ------------------------------------------------------
    turno = "J1"
    flag1 = True
    flag2 = True
    #frame = builder.get_object("Frame1")
    #frame.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(39321,65535,13107))
    tableroJugar = tablero.Tablero()
    labelsJugar = tableroJugar.getResultados()
    prinDatos = tableroJugar.gerPrinTerm()
    # ---------------------------------------------------------
    frames = []
    labels = []
    ImagenesOne = []
    ImagenesTwo = []
    # ---------------------------------------------------------

    mostrarTablero()

    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    #mostrarPregunta(1)2

    Gtk.main()
    

def mostrarPregunta(posicion):
    popUp.set_visible(True)
    #popUp.set_Focus()
    pregunta = builder.get_object("Pregunta")
    pregunta.set_text("Realice la siguiente suma: " + str(prinDatos[posicion])+ " + " + str(labelsJugar[posicion]-prinDatos[posicion]))

def agregarJugar(button):
    global flag1
    global flag2
    global jugador1
    global jugador2
    if flag1 and flag2:
        try:
            jugador1 = agregarJugador()
            ImagenesOne[0].set_visible(True)
            flag1 = False
        except:
            pass
    elif flag2:
        try:
            jugador2 = agregarJugador()
            ImagenesTwo[0].set_visible(True)
            flag2 = False
        except:
            pass
    



def cerrarPop(button):
    global turno
    popUp.set_visible(False)
    if turno == "J1":
        jugador1.setPos(jugador1.getPos() - dado)
        ImagenesOne[jugador1.getPos()].set_visible(True)
        turno = "J2"
    elif turno == "J2":
        jugador2.setPos(jugador2.getPos() - dado)
        ImagenesTwo[jugador2.getPos()].set_visible(True)
        turno = "J1"

def agregarJugador():
    
    try:
        file = open("./src/code/jugadores.txt", 'r')
        print("Lo abrio")
    except FileNotFoundError:
        sys.exit(1)
    lineas = file.readlines()
    for linea in lineas:
        partes = linea.split()
        if partes[0] == entradaID.get_text() and flag1:
            jugadorLocal = jugador.Jugador(partes[0], partes[1])
            break
        elif jugador1.getId() != entradaID.get_text() and partes[0] == entradaID.get_text():
            jugadorLocal = jugador.Jugador(partes[0], partes[1])
            break

    file.close()
    return jugadorLocal
        


def lanzarDado(button):
    if not flag1 and  not flag2:
        global dado 
        global turno
        dado = random.randint(1,6)
        #dado = 44
        labelDado.set_text(str(dado))
        if turno == "J1":
            ImagenesOne[jugador1.getPos()].set_visible(False)
            jugador1.setPos(jugador1.getPos() + dado)
            posactual = jugador1.getPos()
            if (posactual < 43):
                if (posactual%5 == 0):
                    # quiere decir que esta en un monstruo
                    jugador1.setPos(posactual - 5)
                    ImagenesOne[posactual-5].set_visible(True)
                    turno = "J2"
                else:
                    mostrarPregunta(jugador1.getPos())
            else:
                finalizarJuego(jugador1)
        elif turno == "J2":
            ImagenesTwo[jugador2.getPos()].set_visible(False)
            jugador2.setPos(jugador2.getPos() + dado)
            posactual = jugador2.getPos()
            if (posactual < 43):
                if (posactual%5 == 0):
                    # quiere decir que esta en un monstruo
                    if(posactual != 5):
                        jugador2.setPos(posactual - 5)
                        ImagenesTwo[posactual-5].set_visible(True)
                        turno = "J1"
                else:
                    mostrarPregunta(jugador2.getPos())
            else:
                finalizarJuego(jugador2)

def aceptarMensaje(button):
    mensaje.set_visible(False)

def finalizarJuego(jugadorF):
    jugador1.setPos(0)
    jugador2.setPos(0)
    mensaje.set_visible(True)
    mensaje.set_markup("El ganador es " + jugadorF.getNombre())


def mostrarFicha(button):
    prueba = builder.get_object("ImagenTwoF1")
    prueba2 = builder.get_object("ImagenOneF1")
    prueba.set_visible(True)
    prueba2.set_visible(True)


def responderPreg(button):
    global turno
    if turno == "J1":
        if (respuesta.get_text() == str(labelsJugar[jugador1.getPos()])):
            jugador1.setPuntaje(jugador1.getPuntaje()+labelsJugar[jugador1.getPos()])
        else:
            jugador1.setPos(jugador1.getPos() - dado)

        ImagenesOne[jugador1.getPos()].set_visible(True)
        turno = "J2"
    elif turno == "J2":
        if (respuesta.get_text() == str(labelsJugar[jugador2.getPos()])):
            jugador2.setPuntaje(jugador2.getPuntaje()+labelsJugar[jugador2.getPos()])
        else:
            jugador2.setPos(jugador2.getPos() - dado)

        ImagenesTwo[jugador2.getPos()].set_visible(True)
        turno = "J1"
    popUp.set_visible(False)
    #else:
    #    responderPreg2()


def mostrarTablero():

    for i in range(43):

        frames.append(builder.get_object("Frame" + str(i+1)))
        labels.append(builder.get_object("labelF"+str(i+1)))
        ImagenesOne.append(builder.get_object("ImagenOneF" + str(i+1) ))
        ImagenesTwo.append(builder.get_object("ImagenTwoF" + str(i+1) ))

        if ( (i)% 5 == 0 and (i) != 0 ):
            frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(203*257, 50*257, 52*257))
            frames[i].set_shadow_type(Gtk.ShadowType.IN)
            frames[i].set_label(str(i))
            labels[i].set_text(labelsJugar[i])
        elif ((i)%2 == 0 and i != 0 and i != 42):
            frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(204*257, 153*257, 255*257))
            frames[i].set_shadow_type(Gtk.ShadowType.IN)
            frames[i].set_label(str(i))
            labels[i].set_text(str(prinDatos[i])+ " + " + str(labelsJugar[i]-prinDatos[i]))
        elif (i==0):
            frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(153*257, 204*257, 255*257))
            frames[i].set_shadow_type(Gtk.ShadowType.IN)
            frames[i].set_label("Inicio")
        elif ( i==42 ):
            frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(153*257, 204*257, 255*257))
            frames[i].set_shadow_type(Gtk.ShadowType.IN)
            frames[i].set_label("Fin")
        else:
            frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(204*257, 255*257, 153*257))
            frames[i].set_shadow_type(Gtk.ShadowType.IN)
            frames[i].set_label(str(i))
            labels[i].set_text(str(prinDatos[i])+ " + " + str(labelsJugar[i]-prinDatos[i]))

if __name__ == "__main__":
    sys.exit(main())

