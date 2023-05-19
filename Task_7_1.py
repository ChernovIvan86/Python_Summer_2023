              # Task_7_2
# Напишите программу, которая рассчитывает НОК (наим.общ. кратное),
# для списка нат. уральных чисел lst=[12, 24, 36, 48].

# НОК = ab / НОД(a, b),
# где a и b - это натуральные числа, НОД - наибольший общий делитель.


lst=[12, 24, 36, 48]

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
for i in range(0,len(lst_divider)-1):
    lst_divider_j=lst_divider[i]
    for j in range(0,len(lst_divider_j)-1):
        for k in range(2,j//2+1):
            if lst_divider_j[j]%k==0 and lst_divider_j[j]!=k:
                lst_divider_j.pop(j)
    lst_divider[i]=lst_divider_j

print(lst_divider)