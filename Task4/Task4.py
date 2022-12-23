# Реализуйте алгоритм перемешивания списка
import random
list = [1,2,5,6,7,3,8]
print ('Исходный список: ' + str(list))
for i in range(len(list)-1, 0, -1):
    j=random.randint(0,i+1)
    list[i], list[j] = list[j], list[i]
print('Перемешанный список: ' + str(list))