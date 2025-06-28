# -*- coding: utf-8 -*-
"""
Name: dentista.py

Un dentista desea que se cree un programa para su sitio web
donde se le presenten múltiples servicios a los clientes. El cliente elegirá
la opción y se le presentará un total por el servicio que debe pagar el
cliente. Los servicios se dan como se muestra a continuación:
a) Terapia de canal de raíz - $250
b) Chequeo de higiene oral - $50
c) Tratamiento de lesiones de emergencia - $100
d) Chequeo post-procedimiento - $150
e) Chequeos de rutina y consultas - $75
Para pagos anticipados, los clientes tienen un 50% de descuento.
Diseñar un programa que proporcione al cliente toda la información
necesaria y dar un total según lo que el cliente elija.

"""

option = ""
price = 0
answer = ""

while option not in ['a','b','c','d','e']:
    print("a) Terapia de canal de raíz - $250")
    print("b) Chequeo de higiene oral - $50")
    print("c) Tratamiento de lesiones de emergencia - $100")
    print("d) Chequeo post-procedimiento - $150")
    print("e) Chequeos de rutina y consultas - $75")
    
    option = input().lower()
    
    if option not in ['a','b','c','d','e']:
        print("Tecla incorrecta. Por favor, elija una opción entre a) y e).")
    
if option == 'a':
    price = 250
elif option == 'b':
    price = 50
elif option == 'c':
    price = 100
elif option == 'd':
    price = 150
elif option == 'e':
    price = 75
    
while answer not in ["yes", "no", "si", "no"]:
    print("¿Desea pagar por anticipado? (50% de descuento)")
    answer = input().lower()
    
    if answer not in ["yes", "no", "si", "no"]:
        print("Incorrecto. Responda 'si'/'no'/'yes'/'no'.")
        
if answer in ["si", "yes"]:
    price /= 2

print(f"TOTAL ==> {price} €")
    
    
    

