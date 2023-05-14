              # Task_4_3
# Написать программу, которая:
    # получает 2е строки символов, например 'Смеркалось. Было тихо и тепло.'.
    # определить, являются ли эти строки анаграммами (имеют одинаковый набор букв),
    # знаки препинания, цифры, пробелы игнорируются.
    # Вывод: если да, то True, усли нет, то False

st_1='1. Limes, 2. Luster'
st_2='slime, rustle'

s_0=''

tes_1= set()
tes_2= set()

# добавление в мнжество tes_1 СТРОЧНЫХ букв из st_1
for i in st_1:
    if ord(i)>=65+32 and ord(i)<=90+32:
        tes_1.add(i)

# добавление в мнжество tes_1 ЗАГЛАВНЫХ  букв из st_1
for i in st_1:
    if ord(i)>=65 and ord(i)<=90:
        tes_1.add(chr(ord(i)+32))

# добавление в мнжество tes_2 СТРОЧНЫХ букв из st_2
for i in st_2:
    if ord(i)>=65+32 and ord(i)<=90+32:
        tes_2.add(i)

# добавление в мнжество tes_2 ЗАГЛАВНЫХ  букв из st_2
for i in st_2:
    if ord(i)>=65 and ord(i)<=90:
        tes_2.add(chr(ord(i)+32))

print(tes_1)
print(tes_2)

# Симметричная разница a.symmetric_difference(b) или a^b
if len(tes_1.symmetric_difference(tes_2)) == 0:
    print(True)
else: print(False)


