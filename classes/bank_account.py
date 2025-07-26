# -*- coding: utf-8 -*-
"""
name: bank_account.py

Diseña una clase CuentaBancaria que maneje los atributos:

    - Titular (nombre)
    - Saldo
    
Métodos: ingreso, reintegro, consulta de saldo, y transferencia a otra cuenta.

"""

# Clase CuentaBancaria que implementa los atributos y los métodos pedidos
class CuentaBancaria:
    numero = ""
    titular = ""
    saldo = 0.0
    
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        
    def __str__(self):
        return f"Cuenta con número que acaba en: *{self.numero[-3:]}\n \
            Titular: {self.titular}\nSaldo: {self.saldo} €"
            
    def ingresar(self, cantidad):
        self.saldo += cantidad
        
    def reintegrar(self, cantidad):
        self.saldo -= cantidad
    
    def consultar_saldo(self):
        return self.saldo
    
    def transferir(self, other, cantidad_transferida):
        isinstance(other, CuentaBancaria) # CORREGIR
        print(f"Se van a transferir {cantidad_transferida} € de la cuenta \
              *{self.numero[-3:]} a la cuenta *{other.numero[-3:]}. Por favor, espere...")
        
        self.saldo -= cantidad_transferida
        other.saldo += cantidad_transferida
        

# MAIN
opcion = ""
        
