              # Task_6_1
# Написать функцию, которая переводит строку римских цифр в десятичное число.
# Римские цифры: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
# Важно!!!!: в римком числе не может стоят подряд более 3х одинаковых символов.
# Важно!!!!: в римком числе, если предидущий разряд меньше, то его небходимо вычисть из последующего.
# Пример: MMXXIII=2023; MMXXIV=2024; MCMXVII=1917; MCMLXI=1961; MM=2000; MDXXXLXII-1862.

st_2023='MMXXIII'
st_2024='MMXXIV'
st_1917='MCMXVII'
st_1961='MCMLXI'
st_2000='MM'
st_1862='MDCCCLXII'

def ex_rome_in_arab(st):            #объявляем функцию "ex_rome_in_arab" с её аргументом "st"
    lst = []
    # перевод римских цифр в арабские числа
    for i in range(0, len(st)):
        if st[i] == 'M':
            lst.append(1000)
        elif st[i] == 'D':
            lst.append(500)
        elif st[i] == 'C':
            lst.append(100)
        elif st[i] == 'L':
            lst.append(50)
        elif st[i] == 'X':
            lst.append(10)
        elif st[i] == 'V':
            lst.append(5)
        elif st[i] == 'I':
            lst.append(1)
    # lst.append(0) # пускай будет

    print(lst)

    # вычисление арабских значений в разрядах римского числа
    for i in range(0, len(lst)):
        if i >= len(lst) - 1: break  # выход из цикла при условии, что сравнивать не с чем
        if lst[i] < lst[i + 1]:
            lst[i] = lst[i + 1] - lst[i]
            lst.pop(i + 1)            # удалить элемент с индексом "i + 1" в списке "lst"
    print(lst)
    return sum(lst)                   #задаём выходное "sum(lst)" значение функции "ex_rome_in_arab"

st = st_1961                          #задаём значение аргумента "st" для функции "ex_rome_in_arab"
x=ex_rome_in_arab(st)                 #применяем функцию "ex_rome_in_arab"
print(x)
