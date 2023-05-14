              # Task_6_3
# Написать программу, которая:
    # получает строку символов, например 'asd6f78.=,r>t135'
    # печатает три строки: числа; буквы; символы.

# 65-90 - заглавные буквы буквы латинского алфавита (...+32 - строчные)
# 48-57 - арабские цифры
# функция ord определение инд.символа;
# обратная функция получения по числовому коду его номера - chr.

st_0='0asd6f7УFGH8.=,r>t135'
st_cif =''
st_buk=''
st_other=''


for i in st_0:
    # поиск цифр
    if ord(i) >= 48 and ord(i) <= 57:
        st_cif = st_cif + i
    # поиск букв латиницы
    elif ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 65+32 and ord(i) <= 90+32 :
        st_buk = st_buk + i
    # поиск прочих символов
    elif ord(i) > 0 and ord(i) < 48\
            or ord(i) > 57 and ord(i) < 65\
            or ord(i) > 90+32 and ord(i) <= 127 :
        st_other = st_other + i
    else: print('в  ASCII символа - ', i, ' (и кода - ', ord(i), ' нет)')

print(st_cif)
print(st_buk)
print(st_other)

