#Задача 2: Найдите сумму цифр трехзначного числа.

import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

number = int(input('Введите 3-значное число: '))
while number < 100 or number > 999:
    number = int(input('Введите 3 значное число: '))#защита от ввода неподходящего числа
print('Сумма цифра числа = ', number//100 + number%100//10 + number%10)