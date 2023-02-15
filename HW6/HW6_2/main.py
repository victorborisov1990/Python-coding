# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

print('Введите размер массива: ', end="")
count = int(input())
# numbers = [0] * count
numbers = [random.randint(0, 20) for j in range (count)]
print('Введите максимальный диапазон поиска: ', end="")
maximum = int(input())
print('Введите минимальный диапазон поиска: ', end="")
minimum = int(input())
index = []
print('[', end="")
for i in range(count):
    if minimum <= numbers[i] <= maximum:
        index.append(i+1)
    print(f'{i+1}', end=("" if i == count -1 else ",\t"))
print(']')
print(*numbers, sep =",\t")
print(index)
