#!/usr/bin/python
# -*- coding: utf-8 -*-
edad = 0
while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    if edad==15:
        break
    print "Felicidades tienes " + str(edad)
print "el programa termino"