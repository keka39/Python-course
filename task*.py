# Валентина прогуляла лекцию по математике. 
# Преподаватель решил подшутить над нерадивой студенткой и 
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел. 
# Для несложных примеров студентка быстро нашла решения 
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось. 
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
# Решить такое вручную, как вы понимаете, практически нереально. 
# Вот Валентина и обратилась к вам за помощью. 
# Помогите ей 
# Постарайтесь найти самое оптимальное решение.

N = int(input("enter the number: "))

for i in range(1,N + 1):
    if N % i == 0:
        print(i, end="; ")


