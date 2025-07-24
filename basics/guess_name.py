# -*- coding: utf-8 -*-
"""
Name: guess_name.py

Crear un juego simple pero inteligente que almacena un nombre que los
usuarios tendrán que adivinar. Al proporcionar el nombre equivocado,
el programa proporcionará pistas
"""

import random  # para hacer uso del método choice()

lista_nombres = ["Aarón", "Bianca", "Cassandra", "Dmitri", "Elena",
                 "Farah", "Gustavo", "Hiroshi", "Imani", "Javier",
                 "Khadija", "Luciano", "Maomao", "Nikolai", "Olivia",
                 "Pablo", "Quinn", "Rajesh", "Sofía", "Tarik"]

nombre = random.choice(lista_nombres) # choice() elige un elemento aleatorio de la lista
intento = 0
max_intentos = 5

print("LISTA DE NOMBRES:")
for i, nombre in enumerate(lista_nombres, start=1): # indexamos la lista de nombres (str a int)
    print(nombre, end="\t")
    if i % 5 == 0:
        print() # cada 5 elementos de la lista, un salto de línea para mayor legibilidad

print()    
adivina = input("Intenta adivinar el nombre: ")
while adivina != nombre and intento < max_intentos:     # procedimiento de adivinanza para el usuario
    print(f"Incorrecto. Pista: el nombre contiene la letra {random.choice(nombre)}")
    intento += 1    
    adivina = input("Intenta adivinar el nombre: ")

if intento == max_intentos and adivina != nombre:
    print(f"Lo siento, el nombre era {nombre}")
else:
    print(f"Correcto! Lo has conseguido en {intento} intentos!")
    