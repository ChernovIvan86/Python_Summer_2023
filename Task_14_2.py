            # Task_14_1
'''
Напишите рекурсивную функцию, которая вычисляет сумму цифр натурального числа
'''
lst=[]
def summ(num):
    if num==0: # базовое условие (которое останавливает рекурсию)
        return lst
    el=num%10
    lst.append(el)
    num=num//10
    return summ(num)

#num=int(input('Введите число: '))
num=123455
summ(num)
print(sum(lst))
