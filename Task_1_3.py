
x=float(input('ВВЕДИТЕ X:'))
y=float(input('ВВЕДИТЕ Y:'))

if y==0: print('на НУЛЬ делить НЕльзя!','y=', y , 'попробуйте ещё')
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
        elif r = s: print('x+y=', s, 'на втором месте')

    if su>sr and su>sch and su>schch and su>ru and su>rch and  su>rchch and su > uch and su > uchch and su > chchch:
        if s > r : print('x-y=', r, 'на втором месте')