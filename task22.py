# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("введите кол-во элементов первогомножества: "))
set1 = set()
for i in range(n):
    element = int(input("Введите элементы первого множества: "))
    set1.add(element)
print(set1)

m = int(input("введите кол-во элементов второго множества: "))
set2 = set()
for i in range(m):
    element = int(input("Введите элементы второго множества: "))
    set2.add(element)
print(set2)

result = set1.union(set2)
print(result)