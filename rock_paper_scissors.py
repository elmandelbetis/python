# -*- coding: utf-8 -*-
"""
Name: rock_paper_scissors.py

Crear un simple juego de "Piedra, Papel, Tijera" donde la computadora
genera valor al azar y pide al usuario que introduzca su selección. El
resultado debe mostrar si el usuario gana o pierde, o si es un empate.
"""

import random

values = ["piedra", "papel", "tijera"]
cpu = random.choice(values)
player = ""


while player not in values:
    player = input("Introduzca su selección (piedra/papel/tijera): ")
    
if player == cpu:
    print("¡¡EMPATE!!")
elif player == "piedra" and cpu == "tijera":
    print(f"¡¡GANASTE!! CPU: {cpu}")
elif player == "tijera" and cpu == "papel":
    print(f"¡¡GANASTE!! CPU: {cpu}")
elif player == "papel" and cpu == "piedra":
    print(f"¡¡GANASTE!! CPU: {cpu}")
else:
    print(f"¡¡PERDISTE!! CPU: {cpu}")


