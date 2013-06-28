#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 04/05/2013

@author: alumno
'''
import sys
#patrón A
print "(A)"
impresion = ""
for filas in range(10):
    for columnas in range(filas):
        sys.stdout.write("*")
    print ""
#patrón B
print "(B)"
for filas in range(10,0,-1):
    for columnas in range(filas):
        sys.stdout.write("*")
    print ""

