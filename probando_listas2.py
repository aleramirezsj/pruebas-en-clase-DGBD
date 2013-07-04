#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 25/04/2013

@author: alumno
'''
#incorporamos las funciones del sistema operativo
import os
#armo un diccionario con los sistemas operativos como clave y los comandos
#que borran las consola como valores
comandos = {"posix":"clear","nt":"cls"}


personas = {}
localidades= []

def CargarCliente():
    nombre = raw_input("Ingrese el nombre del cliente:")
    apellido = raw_input("Ingrese el apellido del cliente:")
    personas[nombre] = apellido
    
def CargarLocalidad():
    localidad = raw_input("Ingrese el nombre de la localidad:")
    localidades.append(localidad)
    
def ListarLocalidades():
    print "La lista de localidades es:"
    repetir = 1 
    for localidad in localidades:
        print "Localidad Nro:%i %s" % (repetir , localidad)
        repetir += 1
    raw_input("presione <enter> para continuar")


def ListarClientes():
    print "La lista de clientes es:"
    repetir = 1 
    for persona in personas:
        print "Cliente Nro:%i %s %s" % (repetir , persona, personas[persona])
        repetir += 1
    raw_input("presione <enter> para continuar")


while True:
    ##utilizo el diccionario con comandos y pasandole la clave que
    ##retorna os.name que nos dice el sistema operativo en el que estamos
    os.system(comandos[os.name])

    print "********MENU CLIENTES********"
    print "1- Cargar nuevo cliente"
    print "2- Listar clientes"
    print "3- Cargar nueva localidad"
    print "4- Listar localidades"
    print "5- Salir"
    try:
        opcion = input("Ingrese la opción:")
    except:
        raw_input("ERROR, opción no válida, presione <enter> para continuar")
        continue
    if (opcion == 1):
        CargarCliente()
    elif (opcion == 2):
        ListarClientes()
    elif (opcion == 3):
        CargarLocalidad()
    elif (opcion== 4):
        ListarLocalidades()
    elif (opcion == 5):
        for i in range(100):
            print "Adios"
        break
    else:
        raw_input("ERROR, opción no válida, presione <enter> para continuar")





