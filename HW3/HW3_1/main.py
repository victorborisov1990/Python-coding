# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

N = int(input('Введите размер массива: '))
#numbers = [random.randint(-10,10) for i in range (0, N)]
numbers = [0] * N
for i in range (0, N):
    numbers[i] = int(input(f'Введите элемент массива № {i+1}: '))
print(numbers)
count = 0
find = int(input('Какое число вы хотите найти в массиве? '))
for number in numbers:
    if number == find:
        count += 1
if count > 0:
    print(f'Число {find} встречается {count} раз(а)')
else:
    print ('Число не найдено')