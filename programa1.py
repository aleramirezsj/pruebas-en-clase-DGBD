#!/usr/bin/python
# -*- coding: utf-8 -*-

print "CARGA DE ENCUESTA"
nombre=raw_input("Ingrese su nombre:")
apellido=raw_input("Ingrese su apellido:")
print "Hola su nombre es: "+nombre
print "su apellido es: "+apellido
print "Hola "+nombre+" "+apellido
print "Hola %s %s" % (nombre, apellido) 
edad=raw_input("Ingrese su edad:")
dias_de_vida=int(edad)*365
print "tu dias de vida son:"+str(dias_de_vida)
