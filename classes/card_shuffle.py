# -*- coding: utf-8 -*-
"""
Name: card_shuffle.py

Un cliente le ha pedido que cree un programa reutilizable que
contenga funciones reutilizables. La primera situación es crear una
función que cree una baraja de cartas virtual.
Como hay 52 cartas, las cartas con valores numéricos del dos al nueve
estarán representadas por sus respectivos números. Para 10, Jota,
Reina, Rey y As, se requiere usar T, J, Q, K y A.
Después del valor numérico/alfabético habrá otro carácter para
representar el traje. Use la h para corazones, la c para tréboles, la d
para diamantes y la s para picas.
Debes crear una función que no tome ningún parámetro y que utilice
bucles para iterar a través de todas las cartas y almacenarlas con una
abreviatura de dos caracteres en una lista. La función sólo debe
devolver esta lista como resultado.

"""
from random import shuffle

# Clase Carta para definir las cartas que vamos a utilizar en cada baraja
class Carta:

    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    trajes = ["h", "c", "d", "s"]

    def __init__(self, numero, traje):
        if numero not in Carta.valores:
            raise ValueError(f"Valor inválido: {numero!r}")
        if traje not in Carta.trajes:
            raise ValueError(f"Valor inválido: {traje!r}")
            
        self.numero = numero
        self.traje = traje
        
    def __str__(self):
        # Representación legible: "A♥", "T♠", etc.
        simbolos = {"h":"♥", "d":"♦", "c":"♣", "s":"♠"}
        return f"{self.numero}{simbolos[self.traje]}"
    
    def __repr__(self):
        return f"Carta({self.numero!r}, {self.traje!r}"
    
    def __eq__(self, other):
        # Comparación de dos cartas
        return isinstance(other, Carta) and \
            (self.numero, self.traje) == (other.numero, other.traje)
            
    def codigo(self):
        return f"{self.numero}{self.traje}"
            
        
# Clase Baraja para almacenar las 52 cartas que se crean para cada una de ellas

# De esta manera hacemos que el programa sea reutilizable, pudiendo crear todas las barajas
# que queramos
class Baraja:
    
    def __init__(self):
        # Creamos los 52 objetos de tipo Carta
        self.cartas = [Carta(val, traje)
                       for val in Carta.valores
                       for traje in Carta.trajes]
        
    def __len__(self):
        return len(self.cartas)
    
    def __str__(self):
        return " ".join(c.codigo() for c in self.cartas)
    
    def barajar(self):
        shuffle(self.cartas)
        
        
# MAIN
deck = Baraja()
deck.barajar()

print(deck)        
        
        
        

