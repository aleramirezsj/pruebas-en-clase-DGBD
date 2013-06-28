#!/usr/bin/python
# -*- coding: utf-8 -*-
# Tateti por consola ISP20
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.isp20.edu.ar
import sys
import os
#armo un diccionario con los sistemas operativos como clave y los comandos
#que borran las consola como valores
comandos = {"posix":"clear","nt":"cls"}
 
#diccionario con cada una de las posiciones posibles como clave y como valor
#un espacio en blanco que ubicar� la marca de cada jugador cuando la elijan
#para colocar su ficha
 
posiciones_tablero={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
 
#dicionario con las fichas de los 2 jugadores, cada ficha tendr� un posici�n
#asociada, inician en cero los valores, a medida que vayan definiendo posiciones
#se ir�n almacenando en el correspondiente diccionario y clave-ficha
fichas_jugadores = {1:{1:" ",2:" ",3:" "},2:{1:" ",2:" ",3:" "}}
marcas_jugadores = {1:"X",2:"O"}
jugador_actual = 1
ficha_actual = 1
 
def PintarTablero():
    ##utilizo el diccionario con comandos y pasandole la clave que
    ##retorna os.name que nos dice el sistema operativo en el que estamos
    os.system(comandos[os.name])
    print ""
    print "               TA-TE-TI"
    print "Posiciones tablero"
    print posiciones_tablero
    print "Fichas jugadores"
    print "Jugador 1 ",fichas_jugadores[1]
    print "Jugador 2 ",fichas_jugadores[2]
    print"""
                                ======================================      
                                ||        || ||        || ||        ||     
     III  IIIII  IIIIII         ||   """,posiciones_tablero[1],"""  || ||   """,posiciones_tablero[2],"""  || ||   """,posiciones_tablero[3],"""  ||    
     III II   II II  II         ||        || ||        || ||        ||    
     III  II     IIIIII         ======================================    
     III    II   II             ======================================    
     III II  II  II             ||        || ||        || ||        ||    
     III IIIII   II   20        ||   """,posiciones_tablero[4],"""  || ||   """,posiciones_tablero[5],"""  || ||   """,posiciones_tablero[6],"""  ||    
                                ||        || ||        || ||        ||    
                                ======================================    
                                ======================================    
                                ||        || ||        || ||        ||    
                                ||   """,posiciones_tablero[7],"""  || ||   """,posiciones_tablero[8],"""  || ||   """,posiciones_tablero[9],"""  ||    
                                ||        || ||        || ||        ||    
                                ======================================    
""" 
    ##lineas para debug, para poder hacer un seguimiento de la evoluci�n
    ##de los diccionarios
        
tateti = 1 
while tateti == 1:
    PintarTablero()
    if (ficha_actual==0):
        ficha_actual=input("Jugador %i ingrese el numero de ficha a mover: " % jugador_actual)
    pos_jugada = input("Jugador %i: ingrese posicion para la ficha %i: " % (jugador_actual, ficha_actual))
    
    if posiciones_tablero[pos_jugada] == " ":
        posiciones_tablero[pos_jugada]=marcas_jugadores[jugador_actual]
    else:
        raw_input("Casillero incorecto, enter para continuar ")
        continue
    fichas_jugadores[jugador_actual][ficha_actual]=pos_jugada   
    jugador_actual+=1
    if jugador_actual == 3 :
        jugador_actual = 1
        ficha_actual+=1
        if ficha_actual == 4:
            ficha_actual = 0
    PintarTablero()
     
    if posiciones_tablero[1]=="X" and posiciones_tablero[2]=="X" and posiciones_tablero[3]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[1]=="X" and posiciones_tablero[4]=="X" and posiciones_tablero[7]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[1]=="X" and posiciones_tablero[5]=="X" and posiciones_tablero[9]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[2]=="X" and posiciones_tablero[5]=="X" and posiciones_tablero[8]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[3]=="X" and posiciones_tablero[5]=="X" and posiciones_tablero[7]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[4]=="X" and posiciones_tablero[5]=="X" and posiciones_tablero[6]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[3]=="X" and posiciones_tablero[6]=="X" and posiciones_tablero[9]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[7]=="X" and posiciones_tablero[8]=="X" and posiciones_tablero[9]=="X":
        tateti = 0
        print "Ganador jugador 1!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[1]=="O" and posiciones_tablero[2]=="O" and posiciones_tablero[3]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[1]=="O" and posiciones_tablero[4]=="O" and posiciones_tablero[7]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[1]=="O" and posiciones_tablero[5]=="O" and posiciones_tablero[9]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[2]=="O" and posiciones_tablero[5]=="O" and posiciones_tablero[8]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[3]=="O" and posiciones_tablero[5]=="O" and posiciones_tablero[7]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[4]=="O" and posiciones_tablero[5]=="O" and posiciones_tablero[6]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[3]=="O" and posiciones_tablero[6]=="O" and posiciones_tablero[9]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
    elif posiciones_tablero[7]=="O" and posiciones_tablero[8]=="O" and posiciones_tablero[9]=="O":
        tateti = 0
        print "Ganador jugador 2!!!"
        print "GAME OVER"
        raw_input("Enter para salir")
        
        
        
        