
string='AB abz Z'
lst=[]

for i in string:
    lst.append(i)
print(*lst)

for i in range(0,len(lst)):
    num=ord (lst[i])
    if num>=65 and num<=90:
        num= num+1
        if num>=90:
            num = num - 26
        lst[i]=chr(num)

for i in range(0,len(lst)):
    num=ord (lst[i])
    if num>=65+32 and num<=90+32:
        num= num+1
        if num>=90+32:
            num = num - 26
        lst[i]=chr(num)

print(lst)


