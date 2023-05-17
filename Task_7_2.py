              # Task_7_2
# Напишите функцию "def code(string, n)" которая шифрует строку шифром Цезаря,
# Строка содержит латиныкие буквы, пробелы и знаки препинания.
# Пробелы и знаки препинания не меняются.
# Напимер n=1, a->b, B->C, z->a.

# A-Z - 65-90 (...+32 - строчные); a-z - 97-122
# ord () - ф-я возвращает число — код символа.
# chr() - ф-я возвращает смвол по коду.

# Заменяем первые две подстроки "a" в строке c = my_var.replace("a", "A", 2)
# IvAn, RinAt, Olga, Kira

def code(string, n):

    st_code=''
    lst=[]

    for i in string:
        lst.append(i)
    print(lst)

    for i in range(0,len(lst)):
        num=ord (lst[i])
        if num>=65 and num<=90:
            num= num+n
            if num>90:
                num = num - 26
            lst[i]=chr(num)

    for i in range(0,len(lst)):
        num=ord (lst[i])
        if num>=65+32 and num<=90+32:
            num= num+n
            if num>90+32:
                num = num - 26
            lst[i]=chr(num)

    print(lst)

    for i in lst:
        st_code=st_code+i

    return st_code

print(code('AYZ ayz', 1))
