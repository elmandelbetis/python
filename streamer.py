# -*- coding: utf-8 -*-
"""
Name: streamer

Un streamer de YouTube decidió realizar una encuesta en la
que se pidió a los usuarios que dieran su opinión sobre lo que les
gustaría ver en la siguiente transmisión. Su trabajo es crear un
programa que utilice la siguiente información e imprima el resultado de
lo que el usuario eligió, junto con un mensaje de agradecimiento.
¿Qué debería transmitir?
a) Days Gone
b) Resident Evil 2
c) Fortnite
d) Apex Legends
e) Death Stranding
f) ¡Sorpréndenos!
El mensaje final debería ser:
Ha elegido (opción). ¡Aprecio su tiempo y espero verle en la próxima!
"""

print("¿Qué debería transmitir?")
print("a) Days Gone\nb)Resident Evil 2\nc) Fortnite\nd)Apex Legends")
print("e) Death Stranding\nf)¡Sorpréndenos!")

caracter = ""

while caracter not in ['a', 'b', 'c', 'd', 'e', 'f']:
    caracter = input().lower()
    
print(f"Ha elegido la opción {caracter}). ¡Aprecio su tiempo y espero verle en la próxima!")

