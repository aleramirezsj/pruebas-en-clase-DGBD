#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 25/04/2013

@author: alumno
'''

notas = ["Aplazado","Aplazado","Aplazado","No aprobado","No aprobado","Aprobado",
         "Aprobado","Distinguido","Distinguido","Sobresaliente"]
indice = input("Ingrese la nota obtenida:")
print "Su nota es:" + notas[indice-1]
'''
Probando resolver el mismo problema usando If anidados

if indice < 4 :
    print "Aplazado"
elif indice < 6 :
    print "No aprobado"
elif indice < 8 :
    print "Aprobado"
elif indice < 10 :
    print "Distinguido"
elif indice == 10 :
    print "Sobresaliente"
else:
    print "Error número fuera de rango"
'''    
