#!/usr/bin/python
# -*- coding: utf-8 -*-

class Split:
    """Clase realizada en clase"""
    def __init__(self,color):
        self.color = color
        self.temperatura = 0
    
    def SubirTemperatura(self):
        self.temperatura += 1
    
    def BajarTemperatura(self):
        self.temperatura -= 1
        
    def MostrarInformacion(self):
        print "Split de color "+self.color
        print "Temperatura="+str(self.temperatura)
    
misplit=Split("Blanco")
misplit.SubirTemperatura()
misplit.MostrarInformacion()