              # Task_7_3
# Дан двумерный массив чисел в виде списка списков строк.
# Размер массива n-строк, m-столбцов.
# Написать функцию выдающую отсортированный список
# из трёх самых больших значений массива

# import random as random
from random import randint
def search_max(n, m):



    # Задаётся массив и заполняется случайными целыми числами от 0 до 9
    lst=[None]*n
    for i in range(n):
        lst[i]=[None]*m
        for k in range(m):
            lst[i][k] = randint(0, 9)
    print(lst)

    # Задаётся множество и заполняется
    fil=set()
    for i in range(n):
        for k in range(m):
            fil.add(lst[i][k])
    print(fil)

    # Так как множества не индексируются,
    # задаётся доп. список и заполняется из множества
    lst_1=[]
    lst_1=sorted(fil, reverse=True)
    return (lst_1[0],lst_1[1],lst_1[2])

print(search_max(6, 6))
