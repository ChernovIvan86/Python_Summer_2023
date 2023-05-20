f=open("test2.txt",'r', encoding='utf-8')
s=f.readlines()
print(s)
for i in s:
    if i.strip():     # или if i.strip() !='': или if i !='\n':
        print(i.strip())

for i in range(9):
    s = f.readline()
    print(s.strip())


for i in f:
    print(i.strip())
f.close()

f=open("test2.txt",'w', encoding='utf-8')
s='rtyuVVVVVV22'
f.write(s+'\n')
f.write(s+'\n')
f.close()

f=open("test2.txt",'r', encoding='utf-8')
s=f.readlines()
print(s)
f.close()

# прочитать из одного изаписать в другой .txt
f=open("test2.txt",'r', encoding='utf-8')
s=f.readlines()

g=open("test111.txt",'w', encoding='utf-8')
for i in s:
    if set(i) & set('0123456789'):
        pass
    else:
        g.write(i)
        print(i)
f.close()
g.close()

# прочитать из одного каждый второй символ изаписать в другой .txt
f=open("test2.txt",'r', encoding='utf-8')
s=f.read()
f.close()
g=open("test111.txt",'w', encoding='utf-8')
for i in s[::2]:
    g.write(i)
    print(i, end='')
g.close()