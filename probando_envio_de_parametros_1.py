#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Created on 24/08/2012
 
 
@author: Ramirez'''

def Imprimir(diccionario,promedio,tipo_personas):
    print "Los %s ingresados son:" %tipo_personas
    for clave in diccionario:   
        print clave
    print "el promedio de edad de los %s es %0.2f " %(tipo_personas,promedio)
 
def CalcularPromedio(diccionario):
    total=0
    for clave in diccionario:   
        total+=diccionario[clave]
    promedio=float(total)/diccionario.__len__()
    return promedio

 
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
 
 

promedioChicos=CalcularPromedio(chicos)
promedioAdultos=CalcularPromedio(adultos)
promedioAncianos=CalcularPromedio(ancianos)

Imprimir(chicos,promedioChicos,"Chicos")
Imprimir(adultos,promedioAdultos,"Adultos")
Imprimir(ancianos,promedioAncianos, "Ancianos")