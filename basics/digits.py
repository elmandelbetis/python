# -*- coding: utf-8 -*-
"""
Name: digits.py

Se le ha pedido a un programador que cree un programa
simple en el que debe trazar los dígitos del cero al nueve en palabras. El
programa le pedirá a un usuario que introduzca su número, y el
programa imprimirá el mismo en un texto en su lugar. El resultado
deseado es el que se muestra a continuación:
Por favor, introduzca su número: 415602397
Salida: Cuatro Uno Cinco Seis Cero Dos Tres Nueve Siete
"""

digits = {"0":"Cero",
          "1":"Uno",
          "2":"Dos",
          "3":"Tres",
          "4":"Cuatro",
          "5":"Cinco",
          "6":"Seis",
          "7":"Siete",
          "8":"Ocho",
          "9":"Nueve"}

number = input("Por favor, introduzca un número: ")
print("Salida: ", end="")

for i in number:
    print(f"{digits[i]} ", end="")
