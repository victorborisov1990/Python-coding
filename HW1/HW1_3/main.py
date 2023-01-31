# Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написатьпрограмму, которая проверяет счастливость билета. 385916 -> yes, 123456 -> no

import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

number = int(input('Введите 6-значное число: '))
while number < 100000 or number > 999999:
    number = int(input('Введите 6-значное число: '))#защита от ввода неподходящего числа
first_part = number // 1000
fitst_sum = first_part // 100 + first_part % 100 // 10 + first_part % 10
second_part = number % 1000
second_sum = second_part // 100 + second_part % 100 // 10 + second_part % 10
if fitst_sum == second_sum:
    print('yes')
else:
    print('no')