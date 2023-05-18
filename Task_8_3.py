            # Task_8_3
# Дан список слов. Отсортируйте его по числу
# уникальных букв в каждом слове в обратном порядке.
# Например:
    # Вход: ['abab', 'xx', 'aaaaaaaa', 'abcbab'].
    # Выход: ['abcbab', 'abab', 'aaaaaaaa', 'xx'].

lst=['abab', 'xx', 'aaaaaaaa', 'abcbab']
tes={}
lst_unique=[]
lst_num=[]
su=[]

print(lst_unique)

for i in range(0, len(lst)):
    tes=set(lst[i])
    lst_unique.append(tes)
    lst_num.append(len(tes))
    tes = {}
su=list(zip(lst_num, lst))

print(lst_unique)
print(lst_num)
print(su)
print()
print(sorted(su))
print(sorted(su, reverse=True))



