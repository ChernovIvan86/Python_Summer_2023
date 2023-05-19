            # Task_8_3
# Дан список слов. Отсортируйте его по числу
# уникальных букв в каждом слове в обратном порядке.
# Если число уникальных букв одинаково, то порядок алфавитный.
# Например:
    # Вход: ['abab', 'xx', 'aaaaaaaa', 'abcbab'].
    # Выход: ['abcbab', 'abab', 'aaaaaaaa', 'xx'].

lst=['abab', 'xx', 'aaaaaaaa', 'abcbab']
lst.sort()
print(lst)

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
su=sorted(su, reverse=True)

# печать отсортированного списка из списка картежей
lst = []
for i in range(0, len(su)):
    lst.append(su[i][1])

print(*lst)





