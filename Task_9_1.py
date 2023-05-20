            # Task_9_1
# Дан генетический код ДНК (строка состоящая из букв G, C, T, A).
# Постройте РНК, используя принцип замены букв:
# G->C, C->G, T->A, A->T.
# Напишите функцию, которая на вход получает ДНК и возвращает РНК,
# для этого постройте словарь для замены букв.

d={'G':'C', 'C':'G', 'T':'A', 'A':'T'}
st='GCTAATCG'
lst=list(st)
print(lst)

for i in range(0,len(lst)):
    if lst[i]=='G': lst[i]=d['G']
    elif lst[i] == 'C': lst[i] = d['C']
    elif lst[i] == 'T': lst[i] = d['T']
    elif lst[i] == 'A': lst[i] = d['A']
print(lst)
print(''.join(lst))




