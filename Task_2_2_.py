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
index_mi=0

for i in range(1,n):
    lst.append(int(input('Введите НОВЫЙ элемент списка: ')))
    if mi>int(lst[i]):
        mi=int(lst[i])
        index_mi = i
print('элемент', mi, 'с индексом', index_mi,'оказался меньше всех')

                            # Способ III
lst=[]
n=(int(input('Введите число элементов списка: ')))
lst.append(int(input('Введите НОВЫЙ элемент списка: ')))

for i in range(1,n):
    lst.append(int(input('Введите НОВЫЙ элемент списка: ')))

print('Вы ввели список: ', lst)

mi = int(lst[0])
index_mi=0

for i in range(1,n):
    if mi>int(lst[i]):
        mi=int(lst[i])
        index_mi=i
print('элемент', mi, 'с индексом', index_mi,'оказался меньше всех')
