                        # Task_5_3
# Написать программу, которая:
    # печатает ряд чисел Фибоначчи до введённого номера n,
    # например: n=8,    '1,1,2,3,5,8,13,21'.

n=8
s=1
lst=[1,1]
for i in range(0,n-2):
    s=lst[i]+lst[i+1]
    lst.append(s)
print(lst)