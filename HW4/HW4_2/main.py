# /*Найти, какое макс число ягод можно собрать за 1 подход с 3 соседних кустов
# (сумма a[i],a[i+1] и a[i+2]) */
import random
import os  
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

count = int(input('Введите количество кустов: '))
while count < 3 or count > 999:
    count = int(input('Введите количество кустов (3-999): '))
one_action_count = 3 #количество кустов, обрабатываемых за одно действие
kusty_main = [0]*count
for i in range(0, count):
    kusty_main[i] = random.randint(50, 100)
    print (kusty_main[i], end=" ")
kusty = kusty_main + kusty_main[:one_action_count-1]#прибавление в конце куска из начала, чтобы проверялись все соседние "кусты" из "кольца"
print()
print(kusty)# для проверки
max_sum = kusty[0] + kusty[1] + kusty[2]
previous_sum = max_sum
for i in range(1, len(kusty)-one_action_count+1):#проход массива с 1 по n-3+1
    previous_sum = previous_sum - kusty[i-1] + kusty[i+2]#этот алгоритм лучше, когда one_action_count (количество числел подряд большое (сейчас = 3)). 
                                                            #из суммы вычитается крайнее левое и прибавляется крайнее правое значение    
    if previous_sum > max_sum:
        max_sum = previous_sum
#end_plus_begin = kusty[-2:] + kusty[:2] # массив из конца и начала основного массива, которые не были проверены алгоритмом
#оказалось, что проще в конец основного массива добавить недостающие символы из начала
print(max_sum)
