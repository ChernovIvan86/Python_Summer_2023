        # Task_12_3
# Напишите функцию, которая на вход принимает строку
# диапазонов натуральных чисел, напрмер: "1-2,4-4,3-6".
# На выходе функция формирует список натуральных чисел,
# котрые попадают в этоти диапазоны,  нпример:
# [1,2,4,3,4,5,6]
#

lst=[]
st='20-10,4-4,3-6'
lst=st.split(',')
print(lst)

lst_tup=[]
for i in range(0, len(lst)):
    tup = tuple(lst[i].split('-'))
    lst_tup.append(tup)
#[tup = tuple(lst[i].split('-')) lst_tup.append(tup) for i in range(0, len(lst))]
print(lst_tup)
# без использование спискового включения
lst=[]
for i in range(0, len(lst_tup)):
    if int(lst_tup[i][0]) > int(lst_tup[i][1]) + 1:
        for j in range(int(lst_tup[i][1]), int(lst_tup[i][0]) + 1):
            lst.append(j)
    else:
        for j in range(int(lst_tup[i][0]), int(lst_tup[i][1])+1):
            lst.append(j)
print(lst)

# Использование спискового включения единожды
lst=[]
for i in range(0, len(lst_tup)):
    if int(lst_tup[i][0]) > int(lst_tup[i][1]) + 1:
        [lst.append(j) for j in range(int(lst_tup[i][1]), int(lst_tup[i][0])+1)]
    else:
        [lst.append(j) for j in range(int(lst_tup[i][0]), int(lst_tup[i][1])+1)]

print(lst)
