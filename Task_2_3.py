
n=int(input('Введите целое число: '))
a=1
for i in range(1,n+1):
    #print(i)
    a=a*i
print('n!=',n,'!=', a, sep='')