print(123=='123')
print('123'+'123')
print(print(123))
print(123,'123')
print(print)

                       # задать строку st, содержащую: 112225567789
dct={1:3, 2:4, 3:5}                                      # задать пустой словарь
for i in dct:
    dct[i]=dct.get(i, 0)+1                      #
    print(i, '-', dct[i], sep=' ', end='\n')

print(dct)

a='a'
z='0'
if a> z: print(a, 'aaaaaa')
elif z> a: print(z, 'bbbbbb')
#*****************************************************************************
lst=['a','s','d','f','g']
print(lst[-1])
print(lst[-2])
print(lst[-3])
print(lst[-4])
print(lst[-5])

#*****************************************************************************
import math as m                                 # подключить модуль math и бращатся к нему через "m"
a=m.sin(m.radians(0))                            # вычисление sin 00 градусов дуги
b=m.sin(m.radians(90))                           # вычисление sin 90 градусов дуги
c=round (m.sin(m.radians(180)), 1)               # round-необходима для исключения ошибки окр-й при вычислении sin
d=m.sin(m.radians(270))                          # вычисление sin 270 градусов дуги
e=round (m.sin(m.radians(360)), 1)               # round-необходима для исключения ошибки окр-й при вычислении sin

print(a, b, c, d, e, sep='->')
print(m.pi)
#*****************************************************************************
n=7
for i in range(n):print(i)

print(n % 2)

#*****************************************************************************









#*****************************************************************************
