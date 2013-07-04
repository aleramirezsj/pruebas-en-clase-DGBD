# -*- coding: cp1252 -*-
'''Created on 24/08/2012
 
 
@author: Ramirez'''
 
 
continuar="si"
chicos={}
adultos={}
ancianos={}
while continuar=="si":
    nombre=raw_input("Ingrese su nombre:")
    edad=raw_input("Ingrese su edad:")
    if int(edad)<18:
        chicos[nombre]=int(edad)
    elif int(edad)<60:
        adultos[nombre]=int(edad)
    else:
        ancianos[nombre]=int(edad)
    continuar=raw_input("¿Desea ingresar otra persona?(Escriba si o no)")
 
totalChicos=0
totalAdultos=0
totalAncianos=0
 
 
for clave in chicos:   
    totalChicos+=chicos[clave]
promedioChicos=float(totalChicos)/chicos.__len__()
for clave in adultos:   
    totalAdultos+=adultos[clave]
promedioAdultos=float(totalAdultos)/adultos.__len__()
for clave in ancianos:   
    totalAncianos+=ancianos[clave]
promedioAncianos=float(totalAncianos)/ancianos.__len__()
 
print "Los chicos ingresados son:"
for clave in chicos:   
    print clave
print "el promedio de edad de los chicos es "+str(promedioChicos)
print "Los adultos ingresados son:"
for clave in adultos:   
    print clave
print "el promedio de edad de los adultos es "+str(promedioAdultos)
print "Los ancianos ingresados son:"
for clave in ancianos:   
    print clave
print "el promedio de edad de los ancianos es "+str(promedioAncianos)