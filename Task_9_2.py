                    # Task_9_2
# Напишите программу, которая печатает похожие слова.
# Похожие слова содержат равное число гласных,гласные находятся на равных позициях в словах.
# Гласные буквы : а, у, о, ы, и, э, я, ю, ё, е.
# Ввод:
#   x - первое слово,
#   n - число слов для сравнения,
#   далее вводится n слов.

#x=(input('Введите 1е слово: ')).lower()
#n=int(input('Введите число сравниваемых слов: '))
#lst=[x]
#for i in range(1, n+1):
#    lst.append( (input('Введите i-е слово: ')).lower() )
#print((x,n, *lst))
lst_num=[]
lst_i=[]
lst=['питон', 'поросёнок', 'титан', 'итог', 'лавка', 'погост', 'кино']
res=[]

for i in range(0,len(lst)):
    lst_i = list(lst[i])
    for j in range (0,len(lst_i)):
        if lst_i[j]=='а'or lst_i[j]=='у'or lst_i[j]=='о' or lst_i[j]=='ы' or lst_i[j]=='и' or lst_i[j]== 'э'or lst_i[j]=='я'or lst_i[j]=='ю'or lst_i[j]=='ё'or lst_i[j]=='е':
            lst_i[j]='1'
        else: lst_i[j]='0'
    lst_num.append(''.join(lst_i))

for i in range (0,len(lst_num)):
    d=len(lst_num[i])

    lst_num[i]=int(lst_num[i])/(10**d)
print(lst_num)

lst=list(zip(lst_num,lst))
print(lst)

res.append(lst[0][1])

for i in range (1,len(lst)):
    if lst[i][0]==lst[0][0]:
        res.append(lst[i][1])
    else: pass

print('Список похожих слов: ', *res)
# ************************************************
# Остроумно, хотя и громоздко.if в 24 стр.можно и нужно заменить на
# if lst_i[j] in 'ауоыиэяюёе':

s='питон'
def maska(x):
    res=[]
    for i, j in enumerate(x):
        if j in 'ауоыиэяюёе':
            res.append(i)
    return res
print(maska(s))

out=[]
z=['поросёнок', 'титан', 'итог', 'лавка', 'погост', 'кино']
for i in z:
    if maska(i)==maska(s)
        out.append(i)
print(*out)
