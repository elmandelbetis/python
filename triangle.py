# -*- coding: utf-8 -*-
"""
Name: triangle.py
"""

base = int(input("Introduzca tamaño de la base del triángulo: "))

for i in range(1, base + 1):
    
    for j in range(base - i):
        print(" ", end="")
        
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()