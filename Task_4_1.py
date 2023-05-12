
                            # Task_4_1
# Написать калькулятор.
# На вход подаётся строка '1 + 2' или '5 - 3' или '3 * 4' или '10 / 2'.
# Вывести результат математических операций.

st='0123456789*+-/ '
for i in st:
    print('символ: ',i, 'код: ', ord(i))

st=input('введите пример в формате:\nчисло алгебраическое_действие число,\n(кроме возведения в степень и извл. корня)\nнапример 78 + 99 :')

st_cif=''
lst_cif=[]

st_alg=''
lst_alg=[]

for i in st:
    if ord(i) >= 48 and ord(i) <= 57:
        st_cif=st_cif + i
    if ord(i) == 32:
        lst_cif.append(st_cif)
        st_cif=''
lst_cif.append(st_cif)

for i in st:
    if ord(i) >= 42 and ord(i) <= 47:
        st_alg=st_alg+i

print(lst_cif, st_alg)

if st_alg=='+': cal=float(lst_cif[0])+float(lst_cif[2])
if st_alg=='-': cal=float(lst_cif[0])-float(lst_cif[2])
if st_alg=='*': cal=float(lst_cif[0])*float(lst_cif[2])
if st_alg=='/': cal=float(lst_cif[0])/float(lst_cif[2])

print(lst_cif[0], st_alg, lst_cif[2], '=', cal)



#print(ord('*'))



#for i in lst:
#    if ord(i) < 48 or ord(i) > 57
#    print(i)