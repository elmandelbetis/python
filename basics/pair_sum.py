# -*- coding: utf-8 -*-
"""
name: pair_sum

Sums up all the even numbers from 1 to 100
"""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

sum = 0

for i in range(1,100):
    if is_even(i):
        sum += i
        
print(f"The sum equals to {sum}")
