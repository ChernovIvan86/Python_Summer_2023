            # Task_8_2
# На вход подаётся список из списков чисел, например:
    # [[1,5,3], [2,44,1,4], [3,3]].
# Отсортируйте этот список по возрастанию общего числа цифр в каждом подсписке.
# Каждый подсписок отсортировать по убыванию.

lst=[[1,5,3], [2,44,1,4], [3,3], [3,33,1,4]]
lst_unter=[]
st=''

# Сортировка каждого подсписка по убыванию
for i in lst:
    i.sort(reverse=True)
print(lst)


for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
        st=st+str(lst[i][j])
    lst_unter.append(st)
    st =''
print(lst_unter)

for i in range(0, len(lst_unter)):
    lst_unter[i]=len(lst_unter[i])
print(lst_unter)

lst=list(zip(lst_unter, lst))
print(lst)

lst=sorted(lst)
print(lst)

lst_unter=[]
for i in range(0, len(lst)):
    lst_unter.append(lst[i][1])
print(lst_unter)