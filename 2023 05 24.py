
# дана строка 'abcde' какое количество перестановок возможно
from itertools import permutations
s= 'abcde'
for r in range(1,6):
    print(f"{r} - {len(list(permutations(s,r)))}")

#----------------------------------
# time
# Цикл кот будет замедляться
#import time
#x=1e6
#for i in range(0, x, 1e6):
#    t0 = time.time()
#    su = 0
#    for j in range(i*10):
#        su+=j
#    t1 = time.time()
#    print()

# две функции. одна спит 2 сек другая 3 сек
import  time
def f2():
    t0= time.time()
    time.sleep(2)
    t1 = time.time()
    return t1-t0
def f3():
    t0= time.time()
    time.sleep(3)
    t1 = time.time()
    return t1-t0
s2,s3 = 0,0
for i in range(11):
    if i%2: s3 +=f3()
    else: s2 += f2()
    print(s2, s3)

# напишите программу которая



import  locale
print(locale.getlocale())                # посмотреть активный стандарт региона
locale.getlocale(locale.LC_ALL, 'ru')    # перейти на стандарт региона RU

locale.setlocale(locale.LC_ALL,'ru')#, 'en_EN.UTF-8')
birthday = date(1986,09,29)

print(birthday.strftime('%A'))