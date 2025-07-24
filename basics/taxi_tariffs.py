# -*- coding: utf-8 -*-
"""
Name: taxi_tariffs.py

Debes crear una función que calcule la tarifa de un taxi. La tarifa
del taxi se compone de una tarifa base de $3.00 y luego $0.10 por cada
100 metros recorridos. Crea una función que tome la distancia como
único parámetro (en km) y que devuelva el valor de la tarifa total
aplicable. Continúe con un programa para mostrar la naturaleza del
funcionamiento de la función.

"""

def calculate_tariff(distance):
    base = 3.0
    meters = distance * 1000
    price = base + (meters / 100) * 0.10
    
    return price
    

km = -1

while km < 0 or type(km) != float:
    km = float(input("Introduzca distancia (en km): "))
    
total = calculate_tariff(km)

print(f"El precio total del viaje es de {total} €")