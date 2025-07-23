# -*- coding: utf-8 -*-
"""
Name: yo_lo_hice.py

Un adolescente quiso imprimir un simple diseño en Python como
resultado. El diseño que se muestra a continuación fue el resultado:
*
**
***
****
*****
******
*******
********
*********
**********
¡Yo lo hice!
**********
*********
********
*******
******
*****
****
***
**
*
¿Crees que esto se puede hacer usando bucles? Si es así, ¿puedes
codificar el programa?

"""

base = 10

for i in range(base + 1):
    for j in range(i):
        print("*", end="")
        
    print()

print("¡Yo lo hice!")

for i in range(base + 1):
    for j in range(base - i):
        print("*", end="")

    print()