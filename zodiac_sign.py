# -*- coding: utf-8 -*-
"""
Name: zodiac_sign.py

Crear un programa Python que permita al usuario conocer su signo astrológico 
desde la fecha de nacimiento dada
"""

def introducir_fecha():
    fecha = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
    dia_str, mes_str, anio_str = fecha.split('/')
    dia, mes, anio = int(dia_str), int(mes_str), int(anio_str)


def fecha_correcta(dd, mm, aaaa):
    