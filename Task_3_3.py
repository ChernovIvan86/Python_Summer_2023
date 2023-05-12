# на вход подаётся предложение из нескольких слов.
# слова разделены пробелами.
# напечатать первое самое длинное слов.
# напечатать все самые длинные слова.

st='555_555 asd dfg_h hjk_li qwe_rty l7 777_777'         # задаётся строка
st_new=''                             # задаётся строка
lst_new=[]                            # задаётся список
for i in st:                          # задаётся цинл: поочерёдно для каждого i в строке st выполнять:
    if i !=' ': st_new = st_new+i     # если i НЕ= пробелу, выполнять: добавить знач(i) в строку st_new
    elif i == ' ':                    # если же i = пробелу, выполнять:
        lst_new.append(st_new)        # добавить строку st_new в конец списка lst_new
        st_new=''                     # очистить строку st_new
lst_new.append(st_new)                # добавить строку st_new в конец списка lst_new
print(lst_new)                        # печать списка lst_new
print(max(lst_new))                   # печать первый по алфавиту самый длинный по числу символов элемент списка lst_new
lst_new.sort(key=len,reverse=False)   # переставить элементы списка lst_new по возрастанию числа сиволов в них
print(lst_new)                        # печать списка lst_new

#print(lst_new.sort(key=len,reverse=True))   #????????? Почему не отсортировал!!!??????

lst_new.append('0')                    #!!!!!!!!!!!!!!!!!!!!!!!!

for i in lst_new:
    for k in range(0, len(lst_new)-1):                     # специально не заменил на range(len(lst_new))
        if k < len(lst_new)-1:                                  # если k< длины(len) списка lst_new -1 то:
            if len(lst_new[k]) < len(lst_new[k + 1]):               # если длина kого элемента<длины (k+1) элемента то:
                lst_new.remove(lst_new[k])                              # удалить элемент c индексом k из lst_new
            elif len(lst_new[k]) == len(lst_new[k + 1]):            # если же длина kого элемента=длинt (k+1) элемента то:
                len(lst_new[k])==len(lst_new[k])                        # оставить kй элемент без изменений
            else: lst_new.remove(lst_new[k+1])                      # иначе удалить элемент с индексом k+1 из lst_new
        else: break                                             # иначе выйти
print(lst_new)

