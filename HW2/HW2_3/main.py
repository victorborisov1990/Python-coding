# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 10 -> 1 2 4 8

import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

number = int(input('Введите число: '))
n = 1
while n < number:
    print(n)
    n*=2