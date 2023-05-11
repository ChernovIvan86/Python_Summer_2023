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
    for k in range(0, len(lst_new)-1): # специально не заменил на range(len(lst_new))
        if k < len(lst_new)-1:
            if len(lst_new[k]) < len(lst_new[k + 1]):
                lst_new.remove(lst_new[k])
            elif len(lst_new[k]) == len(lst_new[k + 1]):
                len(lst_new[k])==len(lst_new[k])
            else: lst_new.remove(lst_new[k+1])
        else: break
print(i, lst_new.index(i))
print(lst_new)

