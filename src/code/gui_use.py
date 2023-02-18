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

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


builder = Gtk.Builder()
builder.add_from_file("./src/code/GUI.glade")

win = builder.get_object("Ventana")

#frame = builder.get_object("Frame1")
#frame.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(39321,65535,13107))

frames = []
for i in range(49):
    frames.append(builder.get_object("Frame" + str(i+1)))
    if ( (i)% 5 == 0 and (i) != 0 ):
        frames[i-1].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(203*257, 50*257, 52*257))
        frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(204*257, 255*257, 153*257))
        frames[i].set_shadow_type(Gtk.ShadowType.IN)
    elif ((i)%2 == 0 and i != 0 and i != 48):
        frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(204*257, 153*257, 255*257))
        frames[i].set_shadow_type(Gtk.ShadowType.IN)
    elif (i==0 or i == 48):
        frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(153*257, 204*257, 255*257))
        frames[i].set_shadow_type(Gtk.ShadowType.IN)
        frames[i].set_label("Juan")
    else:
        frames[i].modify_bg(Gtk.StateType.NORMAL, Gdk.Color(204*257, 255*257, 153*257))
        frames[i].set_shadow_type(Gtk.ShadowType.IN)


win.connect('destroy', Gtk.main_quit)

win.show_all()
Gtk.main()

