# Способ I
lst=[1, 2, 3]

a=int(lst[0])
b=int(lst[1])
c=int(lst[2])

if a<b and a<c : print(a, '- меньше всех', end='\n')
if b<a and b<c : print(b, '- меньше всех', end='\n')
if c<a and c<b : print(c, '- меньше всех', end='\n')

# Способ II
lst=[]
n=(int(input('Введите число элементов списка: ')))
lst.append(int(input('Введите НОВЫЙ элемент списка: ')))
mi=int(lst[0])
mi_index=0
for i in range(1,n):
    lst.append(int(input('Введите НОВЫЙ элемент списка: ')))
    if mi>int(lst[i]):
        mi=int(lst[i])
        mi_index=mi_index+1
print('элемент', mi, 'с индексом', mi_index,'оказался меньше всех')

