            # Task_14_1
'''
Напишите рекурсивную функцию, которая вычисляет количество (число) цифр введённого натурального числа
'''
tes=set()
def summ(num):
    if num==0: # базовое условие (которое останавливает рекурсию)
        return
    el=num%10
    tes.add(el)
    num=num//10
    return summ(num)

#num=int(input('Введите число: '))
num=123455
summ(num)
print(sum(tes))