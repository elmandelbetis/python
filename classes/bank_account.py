# -*- coding: utf-8 -*-
"""
name: bank_account.py

Diseña una clase CuentaBancaria que maneje los atributos:

    - Titular (nombre)
    - Saldo
    
Métodos: ingreso, reintegro, consulta de saldo, y transferencia a otra cuenta.

"""

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
        
    def reintegro(self, cantidad):
        self.saldo -= cantidad
    
    def consulta_saldo(self):
        return self.saldo
    
    def transferir(self, cuenta2):
        