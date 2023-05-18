              # Task_7_2
# Напишите программу, которая рассчитывает НОК (наим.общ. кратное),
# для списка нат. уральных чисел lst=[12, 24, 36, 48].

# НОК = ab / НОД(a, b),
# где a и b - это натуральные числа, НОД - наибольший общий делитель.


lst=[36,14,12]

# Задаётся список длинной исходного с пустыми списками
lst_divider=[]
lst_divider_j=[]

# нахождение делителей (без единицы и самого числа) каждого числа
for i in lst:
    for j in range(2,i):
        if i%j==0:
            lst_divider_j.append(j)
    lst_divider.append(lst_divider_j)
    lst_divider_j = []
print(lst_divider)

# тест простоты прямым перебором
lst_divider_j = []

for i in range(0, len(lst_divider)):
    lst_divider_j=lst_divider[i]

    for j in range(0, len(lst_divider_j)-1):
        k=2
        while k<int(lst_divider_j[j]):


        for k in range(2,int(lst_divider_j[j])-1):
            if (int(lst_divider_j[j])%k)==0:
                lst_divider_j.pop(j)
#                j=j-1

    print(lst_divider_j)



#for i in range(0, len(lst_divider)):
#    J=len(lst_divider[i])
#    print(J)
#    for j in range(0,J):
#        if (lst_divider[i][J])==1:
#            lst_divider[i][J].a

#    for j in range(len(lst_divider[i])-1):
#$        if j==1:
#            lst_divider[i].remove(j)
#