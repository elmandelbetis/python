# -*- coding: utf-8 -*-
"""
name: circle.py
"""
import math

radius = float(input("Circle radius: "))
area = round(math.pi * radius * radius, 3)

print(f"The area of the inserted circle is {area} m^2")

