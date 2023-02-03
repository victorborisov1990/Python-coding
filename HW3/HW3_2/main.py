# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

numbers = list(map(int, input('Введите числа в массив: ').split(' ')))
print(numbers)
find = int(input('Какое число вы хотите найти в массиве? '))
result = numbers [0]#по умолчанию ответ это 1 элемент массива 
min_dif = abs(numbers [0] - find)#и он же ближайший к искомому (минимальная разница) 
for number in numbers:
    temp = abs(number - find)#вычисляем абсолютную разницу между текущим и искомым
    if temp <= min_dif:
        min_dif = temp #если текущая разница меньше или равна минимальной
        result = number #то это новая минимальная разница, а текущий элемент ближайший к искомому
print(f'Ближайшее к искомому число = {result}')