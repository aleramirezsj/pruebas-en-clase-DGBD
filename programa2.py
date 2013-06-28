#!/usr/bin/python
# -*- coding: utf-8 -*-

#pedimos los datos del producto
print "CARGA DE PRODUCTOS"
codigo=raw_input("Ingrese Código:")
descripcion=raw_input("Ingrese Descripcióñ:")
rubro=raw_input("Ingrese Rubro:")
costo_de_compra=raw_input("Ingrese el Costo:")
precio_al_publico=raw_input("Ingrese el Precio al publico:")

#calculamos la ganancia
ganancia=float(precio_al_publico) - float(costo_de_compra)

#imprimimos la ficha
print "FICHA DEL PRODUCTO"
print "Codigo: "+codigo
print "Descripcion: "+ descripcion,"rubro "+ rubro
print "Costo de compra: "+costo_de_compra, "Precio al publico:"+precio_al_publico
print "Ganancia Por Unidad Vendida en $ %0.2f:" % ganancia

#preguntamos si el producto posee descuento
opcion=raw_input("Posee descuento? (S/N):")

while (opcion.upper()!="S")and(opcion.upper()!="N"):
    print "Error, pulsacion de tecla incorrecta"
    opcion=raw_input("Posee descuento? (S/N):")
if opcion.upper()=="S":
    porcentaje_descuento=raw_input("Ingrese porcentaje de descuento: ")
    #calculamos el descuento en pesos
    descuento_neto=float(precio_al_publico)*float(porcentaje_descuento)/100
    print "Descuento por pago contado: $%0.2f" % (descuento_neto)

else:
    print "Operacion sin descuentos aplicados"
    descuento_neto=0

#calculamos el precio final a pagar
importe_final=float(precio_al_publico)-descuento_neto
print "Importe final: $%0.2f" %(importe_final)