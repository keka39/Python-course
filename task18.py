# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("введите кол-во элементов в массиве: "))
array = []
for i in range(N):
    Ai = int(input("введите элементы массива: "))
    array.append(Ai)
print(array)

X = int(input("введите чисто Х: "))

a = array[i]
for i in array:
    if abs(i - X) < abs(a - X):
        a = array[i]
print(a)

