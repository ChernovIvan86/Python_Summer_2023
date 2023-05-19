            # Task_8_1
# На вход подаётся строка и гентического кода,
# из букв А(аденин), Г(гуанин), Ц(цитозин), Т(тимин).
# подкорректируйте код так что бы:
    # если рядом стоят А и Г, то поменять их местами
    # если рядом стоят Ц и Т, то поместите АГ междуними.

st_dna='АГЦТ'
lst_dna=[]

for i in st_dna:
    lst_dna.append(i)
print(lst_dna)

for i in range(0, len(lst_dna)-1):
    if lst_dna[i]=='А' and lst_dna[i+1]=='Г':
        lst_dna[i] = 'Г'
        lst_dna[i + 1] = 'А'
    elif lst_dna[i]=='Г' and lst_dna[i+1]=='А':
        lst_dna[i] = 'А'
        lst_dna[i + 1] = 'Г'
print(lst_dna)

#x=len(lst_dna)-1
#for i in range(0, x):
i=0
x=len(lst_dna)
while i<=x:

    if lst_dna[i]=='Ц' and lst_dna[i+1]=='Т':
        lst_dna.insert((i+1), 'А')
        lst_dna.insert((i+2), 'Г')
        x=len(lst_dna)

    elif lst_dna[i]=='Т' and lst_dna[i+1]=='Ц':
        lst_dna.insert((i+1), 'А')
        lst_dna.insert((i+2), 'Г')
        x=len(lst_dna)

    i=i+1
    if i == x - 1: break
print(lst_dna)

