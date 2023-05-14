
n=int(input('Введите целое число>3:...'))
while n<4:
    print('внимательно читайте задание')
    n = int(input('Введите целое число>3:...'))
x=0
y=0
                                # !!!!!!!!!!!!!!!!!!!!!!!->
a=[None]                     # введётм пустой список из одного элемента
a=[None]*n                   # введётм n новых указателей на него
a=[['0']*n]*n                # повторяя элемент, который сам является списком,
                             # мы создаём не новый список,
                             # а только лишь новый указатель на него
                                # <-!!!!!!!!!!!!!!!!!!!!!!!

a = ['0'] * n                # введём список из n элементов==подсписков по n элементов '0'
for i in range(n):
    a[i] = ['0'] * n


for y in range(0, n): print(a[y])  # т.е. a-массив, a[y]-элемент-подсписок, значит a[y][x]-элемнт x подсписка a[y]
print('т.е.: "a"-это список-списков, a[y]-элемент-подсписок, значит a[y][x]-элемнт с инд.х подсписка с инд.y" ')

# заполняется нулевая строка
for x in range(0, n):
        a[0][x] = str(int(x)+1)
print(a)

# ****************************************************
conter_yx=0
conter_elem=n




while conter_elem<=(n*n):
# заполняется последний столбец в прямом направлении
    for y in range(conter_yx + 1, n - conter_yx):
        a[y][n - conter_yx - 1] = str(conter_elem + y)


    if conter_elem >=(n*n): break
    conter_elem = conter_elem + y
    print('после n-го столбца conter_elem =', conter_elem)

# заполняется последняя строка в обратном направлении
    for x in range(conter_yx+1,n-conter_yx):
       a[n-conter_yx-1][-x-1] = str(conter_elem + x)


    if conter_elem >= (n * n): break
    conter_elem = conter_elem + x
    print('после n-ой строки conter_elem =', conter_elem)

# заполняется первый столбец в обратном направлении
    for y in range(conter_yx+2, n-conter_yx-1):
        a[-y-1][conter_yx] = str(conter_elem + y)

    if conter_elem >= (n * n): break
    conter_elem = conter_elem + y
    print('после 1-го столбца conter_elem =', conter_elem)

# заполняется вторая строка в прямом направлении
    for x in range(conter_yx+2,n-conter_yx-1):
       a[conter_yx+1][x] = str(conter_elem + x)

    if conter_elem >= (n * n): break
    conter_elem = conter_elem + x
    print('после 2-ой строки conter_elem =', conter_elem)

    conter_yx=conter_yx+1

for y in range(0, n): print(a[y])
print(conter_elem)



