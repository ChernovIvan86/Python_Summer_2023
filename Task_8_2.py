            # Task_8_2
# На вход подаётся список из списков чисел, например:
    # [[1,5,3], [2,44,1,4], [3,3]].
# Отсортируйте этот список по возрастанию общего числа цифр в каждом подсписке.
# Каждый подсписок отсортировать по убыванию.

lst=[[1,5,3], [2,44,1,4], [3,3], [3,33,1,4]]

for i in lst:
    i.sort(reverse=True)
print(lst)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!->
#sort_key=lambda x: (,)
#lst.sort(key=sort_key)
# <-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#print(lst)



for i in range(0, len(lst)):
    "".join(map(str, lst[i]))
    print(lst.sort(key=len("".join(map(str, lst[i])))))
    #print(len(str(lst[i])))
    #print(str(lst[i]))
#    print("".join(map(str, lst[i]))) # map() приводит все элементы списка к строке
                                     # join() склеивает их в одну строку (""-без пробелов)



