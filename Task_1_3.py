
                        # Способ I
x=float(input('ВВЕДИТЕ X:'))
y=float(input('ВВЕДИТЕ Y:'))

if y==0: print('на НУЛЬ делить НЕльзя!','y=', y , 'попробуйте ещё')
elif x==2 and y==2: print('x+y=',x + y,'И', 'x*y=',x * y, 'больше всех')
else:
    s = x + y
    r = x - y
    u = x * y
    ch = x / y
    chch = x // y

    sr=s+r
    su=s+u
    sch=s+ch
    schch=s+chch

    ru=r+u
    rch = r + ch
    rchch = r + chch

    uch = u + ch
    uchch = u + chch

    chchch = ch + chch

    if sr>su and sr>sch and sr>schch and sr>ru and sr>rch and  sr>rchch and sr > uch and sr > uchch and sr > chchch:
        if s > r : print('x-y=', r, 'на втором месте')
        elif r > s: print('x+y=', s, 'на втором месте')

    if su > sr and su > sch and su > schch and su > ru and su > rch and su > rchch and su > uch and su > uchch and su > chchch:
        if s > u: print('x*y=', u, 'на втором месте')
        elif u > s: print('x+y=', s, 'на втором месте')

    if sch > su and sch > sr and sch > schch and sch > ru and sch > rch and sch > rchch and sch > uch and sch > uchch and sch > chchch:
        if s > ch: print('x/y=', ch, 'на втором месте')
        elif ch > s: print('x+y=', s, 'на втором месте')

    if schch > su and schch > sr and schch > sch and schch > ru and schch > rch and schch > rchch and schch > uch and schch > uchch and schch > chchch:
        if s > chch: print('x//y=', chch, 'на втором месте')
        elif chch > s: print('x+y=', s, 'на втором месте')

    if ru > su and ru > sr and ru > sch and ru > schch and ru > rch and ru > rchch and ru > uch and ru > uchch and ru > chchch:
        if r > u: print('x*y=', u, 'на втором месте')
        elif u > r: print('x-y=', r, 'на втором месте')

    if rch > su and rch > sr and rch > sch and rch > schch and rch > ru and rch > rchch and rch > uch and rch > uchch and rch > chchch:
        if r > ch: print('x/y=', ch, 'на втором месте')
        elif ch > r: print('x-y=', r, 'на втором месте')

    if rchch > su and rchch > sr and rchch > sch and rchch > schch and rchch > ru and rchch > rch and rchch > uch and rchch > uchch and rchch > chchch:
        if r > chch: print('x//y=', chch, 'на втором месте')
        elif chch > r: print('x-y=', r, 'на втором месте')

    if uch > su and uch > sr and uch > sch and uch > schch and uch > ru and uch > rch and uch > rchch and uch > uchch and uch > chchch:
        if u > ch: print('x/y=', ch, 'на втором месте')
        elif ch > u: print('x*y=', u, 'на втором месте')

    if uchch > su and uchch > sr and uchch > sch and uchch > schch and uchch > ru and uchch > rch and uchch > rchch and uchch > uch and uchch > chchch:
        if u > chch: print('x//y=', chch, 'на втором месте')
        elif ch > u: print('x*y=', u, 'на втором месте')

    if chchch > su and chchch > sr and chchch > sch and chchch > schch and chchch > ru and chchch > rch and chchch > rchch and chchch > uch and chchch > uchch:
        if ch > chch: print('x//y=', chch, 'на втором месте')
        elif chch > ch: print('x/y=', ch, 'на втором месте')



        # Способ II
x = float(input('ВВЕДИТЕ X:'))
y = float(input('ВВЕДИТЕ Y:'))

if y == 0: print('на НУЛЬ делить НЕльзя!', 'y=', y, 'попробуйте ещё')
elif x == 2 and y == 2: print('x+y=', x + y, 'И', 'x*y=', x * y, 'больше всех')
else:
    lst=[]
    s = x + y
    lst.append(s)

    r = x - y
    lst.append(r)

    u = x * y
    lst.append(u)

    ch = x / y
    lst.append(ch)

    chch = x // y
    lst.append(chch)

    lst.remove(max(lst))
    print(max(lst))