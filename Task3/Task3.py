# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число: '))
dict = {}
for i in range(1, n+1):
    dict[i] = (1+1/i)**i
print(dict, 'сумма значений равна: ', round(sum(dict.values()), 2))