            # Task_9_3
# Произвести частотный анализ текста из файла.
# 1. С помощью словаря и функции get сосчитать
    # сколько раз встречается каждый символ (без учёта регистра) в тексте.
# 2. Отсортировать по убыванию и напечатать первые 10 символов и их частоты.
     # При равенстве частот отсортировать символы по алфавиту.

            # получилось без метода get()
st1='QWERTYUIOP{}[]'+'\n'
st2='asdfghjkl;'+'\n'
st3='ZXCVvvvbnm,./'+'\n'
st4='qwerfghjbnm,['+'\n'
st5 ='polkjhvcwerfghnjm'+'\n'
st6 ='\n'

f_for_Task_9_3 = open("for_Task_9_3", 'w+', encoding='UTF-8')
f_for_Task_9_3.write(st1+st2+st3+st4+st5+st6)
f_for_Task_9_3.close()

f_for_Task_9_3 = open("for_Task_9_3", 'r', encoding='UTF-8')

dct=dict()

for line in f_for_Task_9_3:
    lst=list(line.lower())
    for i in range(0,len(lst)):
        if not lst[i] in dct.keys(): dct[lst[i]]=1
        else: dct[lst[i]]=dct[lst[i]]+1
f_for_Task_9_3.close()
print(dct)

lst=list(zip(dct.keys(), dct.values()))
print(lst)
lst=sorted(lst, key=(lambda x: x[0]), reverse=False)
lst=sorted(lst, key=(lambda x: x[1]), reverse=True)
print(lst)

for i in range(0,9):
    print(lst[i][0],' - ', lst[i][1])
