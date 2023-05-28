            # Task_12_2
# Создайте списковое включение, которе генерирует следующую последовательность:
# 1,2,2,3,3,3, и т.д. до 10

# без использование спискового включения до 10
n = 10
lst_n=[]
st=''

for i in range(1, n):
    for j in range(1, i+1):
        lst_n.append(i)
print(*lst_n)

# Использование спискового включения единожды

new_lst_n=[]

for i in range(1, n):
    [new_lst_n.append(i) for j in range(1, i+1)]
print(*new_lst_n)





