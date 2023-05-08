
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

    if s>r and s>u and s>ch and s>chch: print('x+y=',s, 'больше всех')
    if r>s and r>u and r>ch and r>chch: print('x-y=',r, 'больше всех')
    if u>s and u>r and u>ch and u>chch: print('x*y=',u, 'больше всех')
    if ch>s and ch>r and ch>u and ch>chch: print('x/y=',ch, 'больше всех')
    if chch>s and chch>r and chch>u and chch>ch: print('x/y=',chch, 'больше всех')

