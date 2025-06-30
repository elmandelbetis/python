# -*- coding: utf-8 -*-
"""
Name: campus_univ.py
    
 Un campus universitario ha decidido crear un programa que
determinará la elegibilidad de un solicitante en base a unas pocas
preguntas y condiciones. La universidad en cuestión le ha pedido que
cree un programa para registrar los siguientes datos:
a) Nombre
b) Apellido
c) Edad
d) Puntuación general en su último resultado de la prueba (de 600)
e) Si busca una beca
En base a las siguientes condiciones, se decidirá la elegibilidad para la
admisión y para la beca:
Para la admisión:
● El estudiante debe haber alcanzado al menos un 60% de
puntuación global o superior para ser admitido.
●
Para la beca:
● El estudiante debe tener al menos una puntuación del 80% en el
examen para poder optar a la beca.
Crear un programa con los datos de tres estudiantes diferentes que han
adquirido un 471, 354 y 502 en consecuencia. Imprimir sus resultados
en base a las condiciones anteriores.
"""

name = input("Nombre: ")
surname = input("Apellido: ")
age = input("Edad: ")
score = int(input("Puntuación de la última prueba (de 600): "))

admission = 600 * 0.6
scholarship = 600 * 0.8

if score >= admission:
    print("Usted ha sido admitido")
else:
    print("Usted no ha sido admitido")
    
if score >= scholarship:
    print("Usted ha ganado derecho a beca")
else:
    print("Usted no tiene derecho a beca")

