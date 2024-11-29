# Создаем 2 списка для хранения данных
data_list = list()
tata_list = list()
# Вводим переменную, содержащую информацию о количестве элементов в списке
n = int(input())
#Вводим первые элементы списка и переменные для их хранения
a = 0
b = 1
#Задаем им подходящий тип данных
d = int(a)
g = int(b)
#Вводим переменную для хранения следующих значений необходимого ряда
sum = 0
#Помещаем первые элементы списка в список
data_list.append(d)
data_list.append(g)
#Создаем список при помощи цикла
for i in range (1, n-1):
    sum = data_list[i] + data_list[i-1]
    data_list.append(sum)
    #Выводим список
print(data_list)
# Ищем четные и нечетные числа, преобразуем их соответственно и помещаем в список, после выводим его
for i in range (0,len(data_list)):
    if data_list[i] % 2 == 0:
        data_list[i] = data_list[i]*2
    elif data_list[i] % 2 > 0 or data_list[i] % 2 < 0:
        data_list[i] = data_list[i]**2
print(data_list)
#Ищем минимальный и максимальный элемент списка, выводим их
p = min(data_list)
x = max(data_list)
print('Минимальный элемент',p)
print('Максимальный элемент',x)
print('Количество элементов',len(data_list))
# Импортируем median для поиска медианного значения функции
from statistics import median
med = median (data_list)
#Сравниваем элементы нового списка с медианным значением
for i in range(0,len(data_list)):
    if data_list[i] > med:
        tata_list.append(data_list[i])
#Выводим найденное
print('Количество элементов, большее медианного значения', len(tata_list))
print('(медианное значение)',med)