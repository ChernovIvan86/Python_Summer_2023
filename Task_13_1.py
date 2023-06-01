            # Task_13_1
'''
Создайте функцию-генератор, которая создаёт бесконечную последовательность:
1,-2,3,-4,... .
'''

def ne4et():
    i=1
    while True:
        if i % 2 == 0:
            yield i*(-1)
        else: yield i
        i=i+1

n=7
gen = ne4et()
for i in range(n):
    print(next(gen), end=', ')
