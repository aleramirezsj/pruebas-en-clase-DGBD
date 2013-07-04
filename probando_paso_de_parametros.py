# -*- coding: cp1252 -*-
'''Created on 24/08/2012 
@author: Ramirez'''
 
def calcular_promedio(lista):
    total=0
    promedio=0
    for clave in lista:
        total+=lista[clave]
    if lista.__len__()>0:
        promedio=float(total)/lista.__len__()
    return promedio
 
def imprimir(lista,promedio,categoria):
    if lista.__len__()>0:
        print "Los "+categoria+" ingresados son:"
        for clave in lista:
            print clave
        print "el promedio de edad de los "+categoria+" es "+str(promedio)    
    else:
        print "No hay "+categoria+" ingresados"
 
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
 
promedioChicos=calcular_promedio(chicos)
promedioAdultos=calcular_promedio(adultos)
promedioAncianos=calcular_promedio(ancianos)
 
imprimir(chicos,promedioChicos,"chicos")
imprimir(adultos,promedioAdultos,"adultos")
imprimir(ancianos,promedioAncianos,"ancianos")