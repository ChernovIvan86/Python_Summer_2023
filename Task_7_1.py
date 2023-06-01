              # Task_7_1
# Напишите программу, которая рассчитывает НОК (наим.общ. кратное),
# для списка нат. уральных чисел lst=[12, 24, 36, 48].
# НОК(a, b) - наименьшее число которе делиться и на a, и на b.
# НОК = ab / НОД(a, b),
# где a и b - это натуральные числа, НОД - наибольший общий делитель.


lst=[24, 12, 36, 48]
lst.sort()
print(lst)

tes_div=set()
lst_Div=[]
d={}
tes_Udiv=set()

# нахождение делителей (без единицы) каждого числа
for i in range(0, len(lst)):
    for j in range(2,lst[i]+1):
        if lst[i]%j==0:
            tes_div.add(j)
    lst_Div.append(tes_div)
    tes_div=set()
lst_Div.sort(reverse=False)
print(lst_Div)
# нахождение НОД (наибольший общий делитель)
for i in range(0, len(lst_Div)-1):
    tes_Udiv=lst_Div[0]&lst_Div[i]&lst_Div[i+1]
print(tes_Udiv)
Max_Udiv=max(tes_Udiv)
print(Max_Udiv)
# нахождение и вывод НОК (наим.общ. кратное) # НОК = ab / НОД(a, b).
print(int(max(lst)*lst[lst.index(max(lst))-1]/Max_Udiv))
