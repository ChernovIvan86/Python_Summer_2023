            # Task_14_3
'''
Напишите рекурсивную функцию tri_mirror, которая печатает два треугольника.
Например, для n=3
***
**
*
**
***
Подсказка: одна строка печатается до вызова функции другая после
'''

# Без рекурсивной функции
n=6
for i in range(-n, 0):
    print('*'*abs(i))
for i in range(2, n+1):
    print('*'*abs(i))

# С рекурсивной функцией
import copy
def tri_mirror(num_dir, num_rev, num_stop):
    if num_dir == 0:
        num_rev = num_rev + 1
        if num_rev==num_stop: return # базовое условие (которое останавливает рекурсию)
        print('*' * num_rev)
        return tri_mirror(num_dir, num_rev, num_stop)
    else:
        print('*'*num_dir)
        num_dir=num_dir-1
        return tri_mirror(num_dir, num_rev, num_stop)

# num_dir=int(input('Введите число: '))
num_dir = 4
num_rev = 1
num_stop = copy.deepcopy(num_dir)+1
tri_mirror(num_dir, num_rev, num_stop)
