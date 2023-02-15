# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

print('Введите первый элемент последовательности: ', end=" ")
start = int(input())
print('Введите разность соседних элементов: ', end=" ")
delta = int(input())
print('Введите количество элементов: ', end=" ")
count = int(input())
progerss = []
for i in range (count):
    progerss.append(start + delta * i)
print(progerss)
