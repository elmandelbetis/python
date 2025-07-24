# -*- coding: utf-8 -*-
"""
Name: zodiac_sign.py

Crear un programa Python que permita al usuario conocer su signo astrológico 
desde la fecha de nacimiento dada
"""    

def bisiesto(aaaa):
    return (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 100 == 0 and aaaa % 400 == 0)


def fecha_correcta(dd, mm, aaaa):
    if mm < 0 and mm > 12:
        return False
    elif bisiesto(aaaa) and mm == 2 and dd not in range(1, 30):
        return False
    elif dd not in range(1, 32):
        return False
    
    return True


def obtener_signo(dd, mm):
    if (mm == 3 and dd >= 21) or (mm == 4 and dd <= 20):
        return "Aries"
    elif (mm == 4 and dd >= 21) or (mm == 5 and dd <= 20):
        return "Tauro"
    elif (mm == 5 and dd >= 21) or (mm == 6 and dd <= 20):
        return "Géminis"
    elif (mm == 6 and dd >= 21) or (mm == 7 and dd <= 22):
        return "Cáncer"
    elif (mm == 7 and dd >= 23) or (mm == 8 and dd <= 23):
        return "Leo"
    elif (mm == 8 and dd >= 24) or (mm == 9 and dd <= 22):
        return "Virgo"
    elif (mm == 9 and dd >= 23) or (mm == 10 and dd <= 23):
        return "Libra"
    elif (mm == 10 and dd >= 24) or (mm == 11 and dd <= 22):
        return "Escorpio"
    elif (mm == 11 and dd >= 23) or (mm == 12 and dd <= 21):
        return "Sagitario"
    elif (mm == 12 and dd >= 22) or (mm == 1 and dd <= 20):
        return "Capricornio"
    elif (mm == 1 and dd >= 21) or (mm == 2 and dd <= 19):
        return "Acuario"
    else:
        return "Piscis"
    
        
dia, mes, anio = -1, -1, -1
    
while not fecha_correcta(dia, mes, anio):
    fecha = input("Introduce tu fecha de nacimiento (MM/DD/AAAA): ")
    mes_str, dia_str, anio_str = fecha.split('/')
    dia, mes, anio = int(dia_str), int(mes_str), int(anio_str)
        
signo = obtener_signo(dia, mes)
    
print(f"Tu signo del zodiaco es: {signo}")
    
