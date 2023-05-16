          # Task_5_1
# Ввести число n. Напечатать треугольник Паскаля
# Например n=4, вывод:
#_____________________
# коэф-ты  |  бином   |
#__________|__________|
#1         | (a+b)**0 |
#1 1       | (a+b)**1 |
#1 2 1     | (a+b)**2 |
#1 3 3 1   | (a+b)**3 |
#1 4 6 4 1 | (a+b)**n |

n=6
lst = [[1], [1,1]]
b=[1]

for i in range(2, n+1):
    lst.append([1])
    for k in range(1,i):
        lst[i].append(lst[i-1][k-1]+lst[i-1][k])

    lst[i]=lst[i]+b

#    print(lst[i])
print(lst)
for i in range (n):
    print(*lst[i])

#lst =[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
#o=1
#for i in range (n):
#    o=o*(n/2)
#    print(' '*o, lst[i])



