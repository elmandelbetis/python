# -*- coding: utf-8 -*-
"""
Name: guess_name.py

Crear un juego simple pero inteligente que almacena un nombre que los
usuarios tendrán que adivinar. Al proporcionar el nombre equivocado,
el programa proporcionará pistas
"""

import random

lista_nombres = ["Aarón", "Bianca", "Cassandra", "Dmitri", "Elena",
                 "Farah", "Gustavo", "Hiroshi", "Imani", "Javier",
                 "Khadija", "Luciano", "Maomao", "Nikolai", "Olivia",
                 "Pablo", "Quinn", "Rajesh", "Sofía", "Tarik"]

nombre = random.choice(lista_nombres)
intento = 0
max_intentos = 5



adivina = input("Intenta adivinar el nombre: ")
while adivina != nombre and intento < max_intentos:
    print(f"Incorrecto. Pista: el nombre contiene la letra {random.choice(nombre)}")
    intento += 1    
    adivina = input("Intenta adivinar el nombre: ")

if intento == max_intentos and adivina != nombre:
    print(f"Lo siento, el nombre era {nombre}")
else:
    print(f"Correcto! Lo has conseguido en {intento} intentos!")
    