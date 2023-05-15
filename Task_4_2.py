                            # Task_4_2
# Ввести натуральное число.
# Напечатать квадратную спираль из чисел размером N*N, свёрнутую по часовой стрелке.
# Напечатать квадратную спираль из чисел размером N*N, свёрнутую против часовой стрелки.

N=int(input('Введите натуральное число:...'))
#N = 5

                                # !!!!!!!!!!!!!!!!!!!!!!!->
a=[None]                     # введётм пустой список из одного элемента
a=[None]*N                   # введётм N новых указателей на него
a=[[None]*N]*N               # повторяя элемент, который сам является списком,
                             # мы создаём не новый список,
                             # а только лишь новый указатель на него
                                # <-!!!!!!!!!!!!!!!!!!!!!!!

a = [None] * N               # введём список из N элементов==подсписков по N элементов None
for i in range(N):
    a[i] = [None] * N

conter_elem = 1
sta_sto = 0

while sta_sto < N // 2 :    # т.к. каждый из for отрезает или строку или столбец
	n = N - sta_sto * 2 - 1 # крайний элемент не заполняется
	                        # чтобы выравнять дины столбцов и строк в одном цикле
	# заполняется первая строка кроме последнего элемента
	for x in range(n):
		a[sta_sto][sta_sto + x] = conter_elem
		conter_elem += 1
	# заполняется последний столбец кроме последнего элемента
	for y in range(n):
		a[sta_sto + y][N - 1 - sta_sto] = conter_elem
		conter_elem += 1
	# заполняется ...
	for x in range(n):
		a[N - 1 - sta_sto][N - 1 - sta_sto - x] = conter_elem
		conter_elem += 1
	# заполняется ...
	for y in range(n):
		a[N - 1 - sta_sto - y][sta_sto] = conter_elem
		conter_elem += 1

	sta_sto += 1

if (N % 2): a[conter_yx][conter_yx] = conter_elem   # if n%2: эквивалентен оператору if n % 2 > 0:

for y in range(N): print(a[y])

#*****************************************************************************
# https://dzen.ru/a/X10dF9cJJHMXCDI3 :

N = 5
a = [None] * N
for i in range(N): a[i] = [None] * N
x,y = 0,0
dx,dy = 1,0
for i in range(N * N):
    a[y][x] = i + 1

    if dx:test = x + dx
    else:test = y + dy


    if test < 0 or test == N or a[y + dy][x + dx] != None:
        dx, dy = -dy, dx
    x=x+dx
    y=y+dy

for y in range(N): print(a[y])

